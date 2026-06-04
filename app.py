import streamlit as st
import random

st.set_page_config(
    page_title="Mental Health Support Companion",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>
.main-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 18px 0 8px;
    gap: 10px;
}
.main-title {
    font-size: 1.6rem;
    font-weight: 700;
    text-align: center;
    margin: 0;
    background: linear-gradient(135deg, #1D9E75, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.main-caption {
    font-size: 0.9rem;
    color: #718096;
    text-align: center;
    margin-top: 2px;
}
</style>

<div class="main-header">
    <svg width="54" height="54" viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="8" width="34" height="30" rx="10" fill="#1D9E75"/>
      <circle cx="20" cy="20" r="3.5" fill="white"/>
      <circle cx="34" cy="20" r="3.5" fill="white"/>
      <circle cx="21" cy="20" r="1.5" fill="#0a5c42"/>
      <circle cx="35" cy="20" r="1.5" fill="#0a5c42"/>
      <path d="M19 29 Q27 34 35 29" stroke="white" stroke-width="2" stroke-linecap="round" fill="none"/>
      <line x1="27" y1="8" x2="27" y2="2" stroke="#1D9E75" stroke-width="2.5" stroke-linecap="round"/>
      <circle cx="27" cy="1.5" r="2" fill="#1D9E75"/>
      <rect x="5" y="17" width="5" height="8" rx="2.5" fill="#1D9E75"/>
      <rect x="44" y="17" width="5" height="8" rx="2.5" fill="#1D9E75"/>
      <rect x="22" y="38" width="10" height="5" rx="2" fill="#1D9E75"/>
      <line x1="18" y1="13" x2="22" y2="13" stroke="white" stroke-width="1.2" stroke-linecap="round" opacity="0.5"/>
      <line x1="32" y1="13" x2="36" y2="13" stroke="white" stroke-width="1.2" stroke-linecap="round" opacity="0.5"/>
      <line x1="27" y1="11" x2="27" y2="15" stroke="white" stroke-width="1.2" stroke-linecap="round" opacity="0.5"/>
      <rect x="16" y="43" width="22" height="8" rx="4" fill="#1D9E75" opacity="0.7"/>
    </svg>
    <div class="main-title">Mental Health Support Companion</div>
    <div class="main-caption">A safe space to share, reflect, and find support.</div>
</div>
""", unsafe_allow_html=True)


def get_response(user_input, history):
    msg = user_input.lower()

    # ── Crisis ──
    if any(w in msg for w in ["suicide", "kill myself", "end my life", "self harm", "want to die", "better off dead"]):
        return "💚 I hear you, and I'm really glad you reached out. Your life matters deeply.\n\n🆘 **Please contact immediately:**\n- **988** — Suicide & Crisis Lifeline (call or text)\n- **Text HOME → 741741** — Crisis Text Line\n- **Emergency: 911**\n\nWould you like to talk about what's been going on?"

    # ── Greetings ──
    elif any(w in msg for w in ["hello", "hi", "hey", "salam", "assalam", "helo", "hii"]):
        return random.choice([
            "Hello! So glad you're here. This is a safe, judgment-free space. How are you feeling today? ",
            "Hi there! Welcome. I'm here to listen without any judgment. What's on your mind today? 💙",
            "Hey! I'm really happy you reached out. How has your day been going? 🌱"
        ])

    # ── How are you / chatbot ke baare mein ──
    elif any(w in msg for w in ["how are you", "aap kaisy", "tum kaisy", "you okay", "are you okay"]):
        return "I'm here and fully present for you! More importantly — how are *you* feeling today? I'm all ears. 💚"

    elif any(w in msg for w in ["who are you", "what are you", "tum kaun", "aap kaun", "your name", "tera naam", "apna naam"]):
        return "I'm Serenity — your mental health support companion. 🌿 I'm here to listen, support, and help you navigate your emotions. I'm not a replacement for a therapist, but I'm always here to talk. What's on your mind?"

    elif any(w in msg for w in ["what can you do", "help me", "kya kar sakte", "how can you help"]):
        return "I'm here to support you through anything — stress, anxiety, sadness, relationship problems, family issues, work pressure, loneliness, anger, or just when you need someone to talk to. 💙\n\nJust share what's on your mind — I'll listen without judgment and try my best to help. What would you like to talk about?"

    # ── Anxiety ──
    elif any(w in msg for w in ["anxious", "anxiety", "panic", "panic attack", "worried", "worry", "nervous", "tension", "tense", "ghabrana", "ghabrahat", "darr", "scared", "fear", "phobia"]):
        return random.choice([
            "Anxiety can feel so overwhelming — like your mind just won't slow down. 💙 What you're experiencing is real and valid.\n\nTry this right now: Take a slow breath in for 4 counts, hold for 4, exhale for 4. Repeat 3 times.\n\nWhat's been making you feel anxious lately?",
            "I hear you. Anxiety can be exhausting — your body and mind are working overtime. You're not alone in this. 🌿\n\nCan you tell me more about what's triggering this anxiety? Sometimes talking it through helps us see it more clearly.",
            "Feeling anxious is your mind's way of saying something needs attention. It's okay to feel this way. 💚\n\nIs this anxiety about something specific, or does it feel more like a general heaviness that's hard to shake?"
        ])

    # ── Sadness / Depression ──
    elif any(w in msg for w in ["sad", "sadness", "depressed", "depression", "hopeless", "empty", "numb", "crying", "cry", "tears", "udaas", "dukhi", "rona", "ro raha", "dard", "hurt", "pain", "broken"]):
        return random.choice([
            "I'm so sorry you're feeling this way. That heaviness is real and it matters. 💚\n\nYou don't have to carry this alone. Is there something specific that happened, or has this sadness been building up over time?",
            "Sadness can feel like a weight that just won't lift. I want you to know — what you feel is valid, and you deserve support. 🌿\n\nWould you like to talk about what's been going on? Sometimes sharing it out loud helps.",
            "Feeling empty or numb can be one of the hardest things to explain to others. But I understand. 💙\n\nYou reached out — and that took courage. What's been happening in your life lately?"
        ])

    # ── Stress / Overwhelm ──
    elif any(w in msg for w in ["stress","tension", "stressed", "overwhelmed", "too much", "burnout", "pressure", "burden", "load", "exhausted by", "cant handle", "can't handle", "bohot zyada", "pareshan", "mushkil", "problem", "problems", "issues", "issue"]):
        return random.choice([
            "It sounds like you're carrying a lot right now. That feeling of overwhelm is real and valid. 🌿\n\nLet's slow down for a moment. What feels like the heaviest thing on your plate right now? We can take it one step at a time.",
            "Stress can pile up until everything feels impossible. But you're here, and that's a brave first step. 💙\n\nWhat's been causing the most stress for you lately — is it work, relationships, or something else?",
            "Feeling overwhelmed means you've been strong for too long without a break. You deserve rest and support. 💚\n\nIf you could remove one stressor from your life right now, what would it be?"
        ])

    # ── Loneliness ──
    elif any(w in msg for w in ["lonely", "alone", "isolated", "no one", "nobody", "no friends", "no one cares", "akela", "akeli", "tanha", "koi nahi", "ignored", "left out", "abandoned", "miss", "missing"]):
        return random.choice([
            "Loneliness is one of the most painful feelings — feeling unseen or unheard by others. 💙\n\nBut right here, right now, you are heard. You matter. Can you tell me more about what's making you feel this way?",
            "Feeling alone even when surrounded by people is sometimes the loneliest feeling of all. I understand. 🌿\n\nIs there someone specific you wish you were closer to, or does it feel like a more general disconnect from everyone?",
            "You reached out — which means part of you is looking for connection. That's beautiful and brave. 💚\n\nWhat does loneliness feel like for you right now? I'm here to listen."
        ])

    # ── Anger ──
    elif any(w in msg for w in ["angry", "anger", "frustrated", "rage", "furious", "irritated", "annoyed", "mad", "hate", "gussa", "naraaz", "chidchida", "irritation"]):
        return random.choice([
            "Anger is a completely valid emotion — it usually means something important to you has been crossed or hurt. 💚\n\nI'm not here to judge. What happened that made you feel this way?",
            "It's okay to feel angry. Your feelings are real and they matter. 🌿\n\nSometimes anger is just sadness or hurt wearing a different mask. Would you like to talk about what's underneath this feeling?",
            "Feeling frustrated when things are unfair or painful makes total sense. You don't have to suppress it. 💙\n\nWhat's been going on? Tell me everything — I'm listening."
        ])

    # ── Sleep problems ──
    elif any(w in msg for w in ["sleep", "insomnia", "can't sleep", "cant sleep", "sleepless", "nightmares", "nightmare", "tired", "exhausted", "fatigue", "neend nahi", "neend", "raat ko"]):
        return random.choice([
            "Not being able to sleep is genuinely exhausting — your mind and body both suffer. 🌙\n\nIs it trouble falling asleep, staying asleep, or waking up too early? And has anything changed recently that might be affecting your rest?",
            "Sleep problems often mean our mind is carrying something heavy. 💙\n\nWhat happens when you lie down — does your mind start racing? What kind of thoughts come up?",
            "Rest is so important, and it's hard when it won't come. You deserve peaceful sleep. 🌿\n\nHave you noticed any patterns — like it being worse on certain days or after certain events?"
        ])

    # ── Relationships ──
    elif any(w in msg for w in ["relationship", "girlfriend", "boyfriend", "wife", "husband", "partner", "breakup", "break up", "divorce", "marriage", "love", "crush", "rejection", "rejected", "cheated", "cheating", "fight", "argument", "rishta", "shadi", "mohabbat", "pyaar", "dil toota", "dil"]):
        return random.choice([
            "Relationship pain can cut really deep — it touches our need for love and belonging. 💙\n\nWould you like to share what's been happening? I'm here to listen without judgment.",
            "Whether it's a breakup, conflict, or feeling disconnected from someone you love — it all hurts deeply. 💚\n\nWhat's going on in your relationship right now?",
            "Our relationships shape so much of how we feel about ourselves and the world. 🌿\n\nTell me what's been happening — I want to understand your situation fully."
        ])

    # ── Family problems ──
    elif any(w in msg for w in ["family", "parents", "mother", "father", "mom", "dad", "sister", "brother", "ghar", "gharwale", "ammi", "abu", "bhai", "behan", "relatives", "toxic", "abuse", "abusive"]):
        return random.choice([
            "Family situations can be incredibly complex and emotionally draining. 💙\n\nWhat's been happening at home? I'm here to listen and support you without any judgment.",
            "Our family relationships are some of the most complicated ones we navigate. Whatever you're going through — it's valid. 💚\n\nCan you tell me more about what's been going on?",
            "Home should feel like a safe place — and when it doesn't, it's deeply painful. 🌿\n\nWhat's the situation like for you right now?"
        ])

    # ── Work / Study pressure ──
    elif any(w in msg for w in ["work", "job", "office", "boss", "colleague", "fired", "career", "study", "exam", "fail", "failed", "university", "college", "school", "marks", "grades", "assignment", "deadline", "parhna", "imtihan", "naukri", "kaam"]):
        return random.choice([
            "Work and study pressure can feel relentless — like you're never doing enough. 💙\n\nYou're more than your productivity. What's been happening that's weighing on you?",
            "Career and academic stress is so real and often underestimated. 💚\n\nTell me what's going on — is it a specific situation or a general feeling of pressure?",
            "Whether it's exams, deadlines, or workplace stress — it all takes a real toll. 🌿\n\nWhat's the main thing stressing you out right now?"
        ])

    # ── Confidence / Self esteem ──
    elif any(w in msg for w in ["confidence", "self esteem", "worthless", "useless", "failure", "loser", "not good enough", "ugly", "fat", "hate myself", "hate my", "insecure", "insecurity", "kam aqal", "bewaqoof", "stupid", "dumb"]):
        return random.choice([
            "The way you're talking about yourself worries me — you deserve so much more kindness, especially from yourself. 💚\n\nWhat's been making you feel this way? These feelings usually come from somewhere specific.",
            "Those thoughts about yourself are not the truth — they're pain speaking. You are worthy and you matter. 💙\n\nCan you tell me when these feelings started or what triggered them?",
            "Self-doubt can be so loud and convincing, but it lies. You are enough. 🌿\n\nWhat's been going on that's making you feel this way about yourself?"
        ])

    # ── Grief / Loss ──
    elif any(w in msg for w in ["grief", "grieve", "loss", "lost", "death", "died", "passed away", "dead", "funeral", "mourning", "marna", "mar gaya", "mar gayi", "wafat", "guzar gaye"]):
        return random.choice([
            "I'm so deeply sorry for your loss. Grief has no timeline and no rules — whatever you're feeling is okay. 💙\n\nWould you like to tell me about them, or about how you're coping right now?",
            "Losing someone is one of the heaviest things we carry. Your pain is real and it matters. 💚\n\nI'm here with you in this. What's been hardest for you?",
            "Grief can feel like waves — some moments manageable, others completely overwhelming. 🌿\n\nYou don't have to go through this alone. How are you doing right now?"
        ])

    # ── Motivation / Purpose ──
    elif any(w in msg for w in ["motivation", "motivated", "purpose", "meaning", "lost", "direction", "future", "hope", "hopeless", "give up", "giving up", "quit", "point", "why bother", "what's the point"]):
        return random.choice([
            "Feeling lost or without direction is more common than people admit — and it doesn't mean anything is wrong with you. 💙\n\nWhat used to give you a sense of purpose or excitement? Even if it feels distant now.",
            "Sometimes we go through seasons where everything feels pointless. That's okay — it won't always feel this way. 💚\n\nWhat's been making it hard to find motivation lately?",
            "Losing your sense of purpose can feel terrifying. But you're still here, still searching — and that matters. 🌿\n\nWhat does a meaningful life look like to you, even if it feels far away right now?"
        ])

    # ── Thanks / Positive ──
    elif any(w in msg for w in ["thank", "thanks", "thankyou", "thank you", "helped", "better", "good", "great", "amazing", "shukriya", "meherbani", "acha laga", "theek ho gaya", "feel good"]):
        return random.choice([
            "I'm really glad I could help even a little. 💚 You deserve to feel better — and remember, taking care of your mental health is just as important as your physical health.\n\nI'm always here whenever you need to talk. Take good care of yourself. 🌿",
            "That means so much to hear. You did the hard work by opening up — be proud of yourself. 💙\n\nRemember, I'm always here if things get tough again. You're not alone.",
            "So happy to hear that! 🌱 Keep being gentle with yourself. You deserve all the peace and happiness in the world. Come back anytime you need support. 💚"
        ])

    # ── General / Default ──
    else:
        return random.choice([
            "Thank you for sharing that with me. It takes real courage to open up, and I want you to know I'm fully here with you. 💙\n\nCan you tell me a little more about what's been going on? I want to understand what you're experiencing.",
            "I hear you, and I'm glad you reached out. Whatever you're going through — you don't have to face it alone. 💚\n\nWould you like to share more about what's on your mind?",
            "I'm here and I'm listening — completely without judgment. 🌿\n\nSometimes it helps to just say everything out loud. Tell me what's been happening for you lately.",
            "It sounds like there's something weighing on you. I want to understand. 💙\n\nCan you tell me more about how you've been feeling? Take all the time you need."
        ])


# ── Session state ──
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm really glad you're here. This is a safe, judgment-free space. How are you feeling today? 🌿"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Share what's on your mind...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = get_response(user_input, st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

# ── Sidebar ──
with st.sidebar:
    st.markdown("""
    <div style="display:flex; align-items:center; gap:10px; padding: 4px 0 16px;">
        <svg width="36" height="36" viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="10" y="8" width="34" height="30" rx="10" fill="#1D9E75"/>
          <circle cx="20" cy="20" r="3.5" fill="white"/>
          <circle cx="34" cy="20" r="3.5" fill="white"/>
          <circle cx="21" cy="20" r="1.5" fill="#0a5c42"/>
          <circle cx="35" cy="20" r="1.5" fill="#0a5c42"/>
          <path d="M19 29 Q27 34 35 29" stroke="white" stroke-width="2" stroke-linecap="round" fill="none"/>
          <line x1="27" y1="8" x2="27" y2="2" stroke="#1D9E75" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="27" cy="1.5" r="2" fill="#1D9E75"/>
          <rect x="5" y="17" width="5" height="8" rx="2.5" fill="#1D9E75"/>
          <rect x="44" y="17" width="5" height="8" rx="2.5" fill="#1D9E75"/>
          <rect x="22" y="38" width="10" height="5" rx="2" fill="#1D9E75"/>
          <rect x="16" y="43" width="22" height="8" rx="4" fill="#1D9E75" opacity="0.7"/>
        </svg>
        <div>
            <div style="font-size:15px; font-weight:600; background: linear-gradient(135deg, #1D9E75, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">About</div>
            <div style="font-size:12px; color:#718096;">Mental Health Companion</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("A compassionate AI companion for emotional wellness support.")
    st.markdown("---")
    st.markdown("### 🆘 Crisis Help")
    st.markdown("**988** — Suicide & Crisis Lifeline\n\n**Text HOME → 741741** — Crisis Text Line")
    st.markdown("---")
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Let's start fresh. I'm here to listen. How are you feeling today? 🌿"}
        ]
        st.rerun()
