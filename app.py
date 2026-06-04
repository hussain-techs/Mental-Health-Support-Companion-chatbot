import streamlit as st

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
.sidebar-about-title {
    font-size: 15px;
    font-weight: 600;
    background: linear-gradient(135deg, #1D9E75, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.sidebar-about-sub {
    font-size: 12px;
    color: #718096;
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

# ── Session state ──
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm really glad you're here. This is a safe, judgment-free space. How are you feeling today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Share what's on your mind...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    msg = user_input.lower()
    if any(w in msg for w in ["anxious", "anxiety", "panic", "worried"]):
        response = "Anxiety can feel so overwhelming. What you're experiencing is real and valid. Would you like to try a simple breathing exercise together?"
    elif any(w in msg for w in ["sad", "depressed", "hopeless", "empty"]):
        response = "I'm so sorry you're feeling this way. That heaviness is really difficult to carry. You don't have to go through this alone."
    elif any(w in msg for w in ["stress", "stressed", "overwhelmed", "too much"]):
        response = "It sounds like you're carrying a lot right now. Reaching out like this is a brave first step. What feels heaviest right now?"
    elif any(w in msg for w in ["lonely", "alone", "isolated", "no one"]):
        response = "Loneliness is one of the most painful feelings. Right here, right now — you are heard. You matter."
    elif any(w in msg for w in ["angry", "anger", "frustrated", "furious"]):
        response = "It's completely okay to feel angry. Your feelings are valid. What happened that brought this on?"
    elif any(w in msg for w in ["sleep", "insomnia", "tired", "exhausted"]):
        response = "Not being able to sleep makes everything so much harder. Is the trouble falling asleep or staying asleep?"
    elif any(w in msg for w in ["thank", "thanks", "better", "helped"]):
        response = "I'm really glad to hear that! You deserve to feel better. I'm always here if you need to talk."
    elif any(w in msg for w in ["suicide", "kill myself", "end my life", "self harm"]):
        response = "I hear you and I'm really glad you reached out. Please contact the 988 Suicide & Crisis Lifeline by calling or texting 988. You are not alone."
    else:
        response = "Thank you for sharing that with me. It takes courage to open up. Can you tell me a little more about what's been going on?"

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
            <div class="sidebar-about-title">About</div>
            <div class="sidebar-about-sub">Mental Health Companion</div>
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
            {"role": "assistant", "content": "Let's start fresh. I'm here to listen. How are you feeling today?"}
        ]
        st.rerun()
