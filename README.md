# 🌿 Mental Health Support Chatbot

A fine-tuned LLM that provides **empathetic, emotionally supportive responses** for stress, anxiety, and emotional wellness — built with Hugging Face Transformers and the EmpatheticDialogues dataset.

---

## 🏗️ Architecture

```
mental_health_chatbot/
├── train.py        ← Fine-tuning pipeline (DistilGPT2 on EmpatheticDialogues)
├── chatbot.py      ← Inference engine + safety filters
├── cli.py          ← Command-line interface
├── app.py          ← Streamlit web interface
└── requirements.txt
```

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Fine-tune the model

```bash
python train.py
```

This will:
- Download **EmpatheticDialogues** from Hugging Face Hub automatically
- Fine-tune **DistilGPT2** for 3 epochs on 5,000 conversation samples
- Save the model to `./model_output/`
- Run a quick inference test

Training takes ~15–30 minutes on CPU, ~5 minutes on GPU.

### 3a. Launch the CLI

```bash
python cli.py
# Or specify a custom model directory:
python cli.py --model-dir ./model_output
```

### 3b. Launch the Streamlit Web App

```bash
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

---

## 🤗 Dataset: EmpatheticDialogues

| Property | Value |
|---|---|
| Source | Facebook AI Research |
| HuggingFace ID | `empathetic_dialogues` |
| Size | 25,000 conversations |
| Labels | 32 emotion categories |
| Task | Empathetic response generation |

The dataset contains human conversations where one speaker expresses an emotion and the other responds empathetically. Each sample includes:
- **context** — the emotion label (e.g., "anxious", "sad", "grateful")
- **prompt** — the emotional statement
- **utterance** — the empathetic response

---

## 🧠 Model: DistilGPT2

| Property | Value |
|---|---|
| Parameters | ~82M |
| Architecture | Causal Language Model |
| Fine-tuning task | Next-token prediction on dialogue |
| Max context | 256 tokens |

### Why DistilGPT2?
- **Fast to fine-tune** — runs on CPU in reasonable time
- **Small footprint** — easy to deploy
- **Good baseline** — pre-trained language understanding

### Upgrading to larger models
Change `MODEL_NAME` in `train.py`:
```python
MODEL_NAME = "EleutherAI/gpt-neo-125M"   # 125M params, better quality
MODEL_NAME = "EleutherAI/gpt-neo-1.3B"   # 1.3B params, requires GPU
MODEL_NAME = "mistralai/Mistral-7B-v0.1" # 7B params, requires ~16GB VRAM
```

---

## 🛡️ Safety Features

### Crisis Detection
The chatbot automatically detects crisis keywords (suicidal ideation, self-harm) and immediately surfaces emergency resources:
- 988 Suicide & Crisis Lifeline (US)
- Crisis Text Line (Text HOME to 741741)
- International crisis center directory

### Graceful Fallback
If the fine-tuned model produces low-quality output, the system falls back to a **rule-based empathy engine** with pattern-matched responses for:
- Anxiety & panic
- Depression & sadness
- Stress & overwhelm
- Loneliness & isolation
- Anger & frustration
- Sleep difficulties

### Professional Help Prompting
When users mention seeking professional help, the bot provides guidance on finding licensed therapists.

---

## 🎓 Training Details

```python
TrainingArguments(
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=5e-5,
    warmup_steps=100,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    load_best_model_at_end=True,  # early stopping
    fp16=True,  # if GPU available
)
```

**Prompt format:**
```
You are a warm, compassionate mental health support companion...

Emotion Context: anxious
Person: I've been feeling really worried about everything lately.
Supporter: [model generates here]
```

---

## 🖥️ CLI Features

- 🎨 Colorized ANSI terminal output
- ⌨️ Typewriter effect for bot responses
- 🔄 `reset` command to start fresh
- ❓ `help` command for usage tips
- 🧘 Check-in reminder every 5 turns

## 🌐 Streamlit Features

- 💬 Mood quick-start buttons (Sad, Anxious, Overwhelmed, Tired, Numb)
- 🆘 Sidebar crisis resources (always visible)
- 🧘 Box breathing exercise tool
- 🔄 Reset conversation button
- 📱 Mobile-friendly dark theme

---

## ⚠️ Important Disclaimer

This chatbot is an **AI support companion**, not a licensed mental health professional. It is not a substitute for professional therapy, counseling, or psychiatric care.

If you or someone you know is in crisis, please contact:
- **988** (Suicide & Crisis Lifeline, US)
- **Crisis Text Line**: Text HOME to 741741
- **Emergency services**: 911 or local equivalent

---

## 📚 References

- [EmpatheticDialogues Paper](https://arxiv.org/abs/1811.00207) — Rashkin et al., Facebook AI
- [Hugging Face Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer)
- [DistilGPT2](https://huggingface.co/distilgpt2)
