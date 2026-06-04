"""
Mental Health Support Chatbot - Fine-Tuning Script
Dataset: EmpatheticDialogues (Facebook AI)
Model: DistilGPT2 (lightweight, fast to fine-tune)
"""

import os
import json
import torch
import logging
from datasets import load_dataset, Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback,
)
from torch.utils.data import DataLoader
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
MODEL_NAME = "distilgpt2"          # swap to "EleutherAI/gpt-neo-125M" for slightly larger
OUTPUT_DIR = "./model_output"
MAX_LENGTH = 256
BATCH_SIZE = 4
EPOCHS = 3
LEARNING_RATE = 5e-5
WARMUP_STEPS = 100

# Empathy-focused system prefix for every training sample
SYSTEM_PREFIX = (
    "You are a warm, compassionate mental health support companion. "
    "You listen carefully, validate feelings, and respond with empathy and kindness. "
    "You never judge, always encourage, and gently suggest professional help when needed.\n\n"
)


# ─────────────────────────────────────────────
# DATASET PREPARATION
# ─────────────────────────────────────────────

def load_empathetic_dialogues():
    """Load and preprocess the EmpatheticDialogues dataset."""
    logger.info("Loading EmpatheticDialogues dataset...")
    dataset = load_dataset("empathetic_dialogues")
    return dataset


def format_conversation(example):
    """
    Format a single EmpatheticDialogues example into a conversational prompt.
    The dataset has: conv_id, utterance_idx, context (emotion), prompt, utterance, speaker_idx
    """
    emotion = example.get("context", "neutral")
    prompt = example.get("prompt", "")
    response = example.get("utterance", "")

    # Build a gentle, empathetic conversation turn
    text = (
        f"{SYSTEM_PREFIX}"
        f"Emotion Context: {emotion}\n"
        f"Person: {prompt}\n"
        f"Supporter: {response}"
        f"<|endoftext|>"
    )
    return {"text": text}


def prepare_dataset(dataset, tokenizer, split="train", max_samples=5000):
    """Tokenize and prepare dataset split."""
    data = dataset[split]

    # Limit samples for faster training (remove cap for full fine-tuning)
    if max_samples and len(data) > max_samples:
        data = data.select(range(max_samples))

    # Format conversations
    formatted = data.map(format_conversation, remove_columns=data.column_names)

    # Tokenize
    def tokenize(examples):
        tokens = tokenizer(
            examples["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding="max_length",
        )
        tokens["labels"] = tokens["input_ids"].copy()
        return tokens

    tokenized = formatted.map(tokenize, batched=True, remove_columns=["text"])
    tokenized.set_format("torch")
    return tokenized


# ─────────────────────────────────────────────
# MODEL SETUP
# ─────────────────────────────────────────────

def load_model_and_tokenizer(model_name: str):
    """Load pretrained model and tokenizer."""
    logger.info(f"Loading model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # GPT-style models need a pad token
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.resize_token_embeddings(len(tokenizer))

    return model, tokenizer


# ─────────────────────────────────────────────
# TRAINING
# ─────────────────────────────────────────────

def train(model_name: str = MODEL_NAME):
    """Main training function."""

    # Load model
    model, tokenizer = load_model_and_tokenizer(model_name)

    # Load and prepare data
    raw_dataset = load_empathetic_dialogues()
    train_dataset = prepare_dataset(raw_dataset, tokenizer, split="train", max_samples=5000)
    eval_dataset = prepare_dataset(raw_dataset, tokenizer, split="validation", max_samples=500)

    logger.info(f"Train samples: {len(train_dataset)}")
    logger.info(f"Eval samples:  {len(eval_dataset)}")

    # Training arguments
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        warmup_steps=WARMUP_STEPS,
        learning_rate=LEARNING_RATE,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=50,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        fp16=torch.cuda.is_available(),   # use mixed precision if GPU available
        push_to_hub=False,
        report_to="none",                  # disable wandb/mlflow for simplicity
    )

    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,  # causal LM, not masked LM
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],
    )

    logger.info("Starting training...")
    trainer.train()

    # Save final model + tokenizer
    logger.info(f"Saving model to {OUTPUT_DIR}")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    logger.info("Training complete! ✓")
    return OUTPUT_DIR


# ─────────────────────────────────────────────
# QUICK INFERENCE TEST
# ─────────────────────────────────────────────

def test_model(model_dir: str, prompt: str):
    """Quick inference test after training."""
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    model.eval()

    input_text = f"{SYSTEM_PREFIX}Person: {prompt}\nSupporter:"
    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.3,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = generated.split("Supporter:")[-1].strip()
    print(f"\n[Test] User: {prompt}")
    print(f"[Test] Bot:  {response}\n")
    return response


if __name__ == "__main__":
    model_dir = train()
    test_model(model_dir, "I've been feeling really overwhelmed lately with everything going on.")
