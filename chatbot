"""
Mental Health Chatbot - Inference Engine
Handles response generation with safety filters and empathy logic.
"""

import os
import re
import torch
import logging
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

SYSTEM_PREFIX = (
    "You are a warm, compassionate mental health support companion. "
    "You listen carefully, validate feelings, and respond with empathy and kindness. "
    "You never judge, always encourage, and gently suggest professional help when needed.\n\n"
)

# Crisis keywords that trigger immediate safety messaging
CRISIS_KEYWORDS = [
    "suicide", "suicidal", "kill myself", "end my life", "don't want to live",
    "self-harm", "hurt myself", "cutting", "overdose", "no reason to live",
    "want to die", "better off dead",
]

CRISIS_RESPONSE = (
    "I hear you, and I'm really glad you reached out. What you're feeling matters deeply. "
    "Please know that you're not alone in this moment.\n\n"
    "🆘 **If you're in immediate danger, please contact:**\n"
    "• **Crisis Text Line**: Text HOME to 741741\n"
    "• **National Suicide Prevention Lifeline**: 988 (US)\n"
    "• **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/\n\n"
    "I'm here to listen. Would you like to tell me more about what you're going through?"
)

PROFESSIONAL_HELP_TRIGGER = [
    "therapist", "psychologist", "professional help", "see someone", "get help",
    "medication", "psychiatrist", "counselor",
]


class MentalHealthChatbot:
    """
    Inference wrapper for the fine-tuned mental health support chatbot.
    Falls back to a rule-based empathy engine if no fine-tuned model is found.
    """

    def __init__(self, model_dir: str = "./model_output", use_fallback: bool = True):
        self.model_dir = model_dir
        self.use_fallback = use_fallback
        self.model = None
        self.tokenizer = None
        self.conversation_history: List[Dict] = []

        self._load_model()

    def _load_model(self):
        """Load fine-tuned model, fall back gracefully if unavailable."""
        if os.path.exists(self.model_dir):
            try:
                logger.info(f"Loading fine-tuned model from {self.model_dir}")
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
                self.model = AutoModelForCausalLM.from_pretrained(self.model_dir)
                self.model.eval()
                logger.info("Fine-tuned model loaded successfully ✓")
            except Exception as e:
                logger.warning(f"Could not load fine-tuned model: {e}")
                if self.use_fallback:
                    self._load_base_model()
        elif self.use_fallback:
            logger.info("No fine-tuned model found. Using base DistilGPT2 with empathy prompting.")
            self._load_base_model()

    def _load_base_model(self):
        """Load base DistilGPT2 as fallback."""
        try:
            self.tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model = AutoModelForCausalLM.from_pretrained("distilgpt2")
            self.model.eval()
            logger.info("Base DistilGPT2 loaded as fallback ✓")
        except Exception as e:
            logger.error(f"Could not load any model: {e}")

    def _check_crisis(self, text: str) -> bool:
        """Detect potential crisis language."""
        text_lower = text.lower()
        return any(kw in text_lower for kw in CRISIS_KEYWORDS)

    def _check_professional_help_request(self, text: str) -> bool:
        """Detect if user is asking about professional help."""
        text_lower = text.lower()
        return any(kw in text_lower for kw in PROFESSIONAL_HELP_TRIGGER)

    def _build_prompt(self, user_message: str) -> str:
        """Build a contextualized prompt from conversation history."""
        history_text = ""
        # Include last 3 turns for context
        recent_history = self.conversation_history[-6:] if len(self.conversation_history) > 6 else self.conversation_history
        for turn in recent_history:
            if turn["role"] == "user":
                history_text += f"Person: {turn['content']}\n"
            else:
                history_text += f"Supporter: {turn['content']}\n"

        prompt = f"{SYSTEM_PREFIX}{history_text}Person: {user_message}\nSupporter:"
        return prompt

    def _generate_response(self, prompt: str) -> str:
        """Generate response using the loaded model."""
        if self.model is None or self.tokenizer is None:
            return self._rule_based_response(prompt)

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=400,
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=120,
                do_sample=True,
                temperature=0.75,
                top_p=0.92,
                top_k=50,
                repetition_penalty=1.4,
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        full_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract only the new "Supporter:" part
        if "Supporter:" in full_text:
            response = full_text.split("Supporter:")[-1].strip()
            # Clean up any trailing incomplete sentences
            response = self._clean_response(response)
        else:
            response = full_text[len(prompt):].strip()
            response = self._clean_response(response)

        return response if response else self._rule_based_response(prompt)

    def _clean_response(self, text: str) -> str:
        """Clean and validate generated response."""
        # Remove repeated "Person:" lines the model may hallucinate
        if "Person:" in text:
            text = text.split("Person:")[0].strip()
        # Ensure response ends at a sentence boundary
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        clean = " ".join(sentences[:4]).strip()  # max 4 sentences
        # Remove stray tokens
        clean = re.sub(r'<\|.*?\|>', '', clean).strip()
        return clean

    def _rule_based_response(self, user_message: str) -> str:
        """
        Fallback empathetic response engine using pattern matching.
        Used when model generation fails or produces low-quality output.
        """
        msg = user_message.lower()

        if any(w in msg for w in ["anxious", "anxiety", "panic", "worried", "worry"]):
            return (
                "Anxiety can feel so overwhelming, like your mind won't slow down. "
                "What you're experiencing is real, and it makes sense that you'd feel this way. "
                "Would you like to try a simple grounding technique together? "
                "Sometimes focusing on what we can see, hear, and touch helps calm the nervous system."
            )
        elif any(w in msg for w in ["sad", "depressed", "depression", "hopeless", "empty"]):
            return (
                "I'm so sorry you're feeling this way. That heaviness and emptiness is really difficult to carry. "
                "You don't have to go through this alone. "
                "Is there one small thing today that brought even a tiny moment of comfort — "
                "a cup of tea, a song, a pet?"
            )
        elif any(w in msg for w in ["stress", "stressed", "overwhelmed", "too much", "burnout"]):
            return (
                "It sounds like you're carrying a lot right now. Feeling overwhelmed is a signal that "
                "you need some care — and reaching out like this is a brave first step. "
                "What feels like the heaviest thing on your plate at the moment?"
            )
        elif any(w in msg for w in ["lonely", "alone", "isolated", "no one", "nobody"]):
            return (
                "Loneliness is one of the most painful feelings there is. I want you to know "
                "that right here, right now, you are heard. You matter. "
                "What does connection look like for you — is there someone in your life "
                "you've been thinking about reaching out to?"
            )
        elif any(w in msg for w in ["angry", "anger", "frustrated", "rage", "furious"]):
            return (
                "It's completely okay to feel angry — anger often comes from unmet needs or things "
                "that feel deeply unfair. Your feelings are valid. "
                "When you're ready, I'd love to understand what's underneath that anger. "
                "What happened?"
            )
        elif any(w in msg for w in ["sleep", "insomnia", "can't sleep", "tired", "exhausted"]):
            return (
                "Not being able to sleep makes everything so much harder. "
                "Your mind and body are clearly working overtime. "
                "Is the trouble falling asleep, staying asleep, or waking up too early? "
                "I'd like to help you think through what might be going on."
            )
        elif any(w in msg for w in ["thank", "thanks", "helped", "better", "good"]):
            return (
                "I'm really glad to hear that. You deserve to feel better. "
                "Remember, taking care of your mental health is just as important as physical health. "
                "I'm always here if you need to talk."
            )
        else:
            return (
                "Thank you for sharing that with me. It takes courage to open up about how you're feeling. "
                "I'm here to listen without judgment. "
                "Can you tell me a little more about what's been going on for you?"
            )

    def chat(self, user_message: str) -> Dict:
        """
        Main chat method. Returns response dict with text and metadata.
        """
        # Safety check first
        if self._check_crisis(user_message):
            response_text = CRISIS_RESPONSE
            response_type = "crisis"
        else:
            # Generate empathetic response
            prompt = self._build_prompt(user_message)
            response_text = self._generate_response(prompt)

            # Append professional help note if needed
            if self._check_professional_help_request(user_message):
                response_text += (
                    "\n\nSpeaking with a licensed therapist or counselor can provide "
                    "personalized support that goes beyond what I can offer. "
                    "Psychology Today's therapist finder (psychologytoday.com/us/therapists) "
                    "is a great place to start."
                )
            response_type = "empathetic"

        # Update history
        self.conversation_history.append({"role": "user", "content": user_message})
        self.conversation_history.append({"role": "assistant", "content": response_text})

        return {
            "response": response_text,
            "type": response_type,
            "turn": len(self.conversation_history) // 2,
        }

    def reset(self):
        """Clear conversation history for a fresh session."""
        self.conversation_history = []
        logger.info("Conversation history cleared.")
