"""
streamlit_app.py
----------------
This is the Streamlit web interface for Rubi AI chatbot.
Female-style elegant UI with soft pink/purple gradient theme.

Run with:
    python -m streamlit run app/streamlit_app.py
"""

import sys
from pathlib import Path

import streamlit as st

# Add src/ to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from chatbot import RubiAIChatbot


# ------------------------------------------
# Page Configuration
# ------------------------------------------
st.set_page_config(
    page_title="Rubi AI - Your Assistant",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded",
)


# ------------------------------------------
# Female-Style Custom CSS
# ------------------------------------------
st.markdown("""
<style>
    /* Import elegant Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Dancing+Script:wght@600;700&display=swap');

    /* Global font */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Soft pink gradient background */
    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #FFC1E3 30%, #E0C3FC 60%, #FFC1E3 100%);
        background-attachment: fixed;
    }

    /* Main container - frosted glass card */
    .main .block-container {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 2.5rem 3rem;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 15px 50px rgba(255, 105, 180, 0.2),
                    0 0 0 1px rgba(255, 182, 220, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.7);
    }

    /* Main Header - elegant cursive with glow */
    .main-header {
        font-family: 'Dancing Script', cursive;
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(90deg, #FF6FB5 0%, #C56CFF 50%, #FF6FB5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.2rem;
        line-height: 1.2;
        filter: drop-shadow(0 4px 10px rgba(255, 105, 180, 0.25));
    }

    /* Sub header */
    .sub-header {
        font-family: 'Poppins', sans-serif;
        font-size: 1.05rem;
        font-weight: 300;
        color: #9B6AA8;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: 0.5px;
    }

    /* Decorative divider */
    .divider-hearts {
        text-align: center;
        color: #FF6FB5;
        font-size: 1.2rem;
        margin: 1rem 0 2rem 0;
        letter-spacing: 0.5rem;
    }

    /* Chat messages - soft rounded bubbles */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 22px !important;
        border: 1.5px solid rgba(255, 182, 220, 0.6) !important;
        padding: 1.1rem 1.3rem !important;
        margin-bottom: 0.9rem !important;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.12) !important;
        transition: all 0.3s ease;
    }

    .stChatMessage:hover {
        box-shadow: 0 6px 20px rgba(255, 105, 180, 0.2) !important;
        transform: translateY(-2px);
    }

    /* Sidebar - pink gradient with border */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFE4F0 0%, #F5D5FF 50%, #FFE4F0 100%);
        border-right: 3px solid rgba(255, 182, 220, 0.6);
        box-shadow: 5px 0 20px rgba(255, 105, 180, 0.1);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #C56CFF;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        text-shadow: 0 1px 3px rgba(255, 105, 180, 0.15);
    }

    /* Sample question buttons */
    section[data-testid="stSidebar"] .stButton > button {
        background: rgba(255, 255, 255, 0.95);
        color: #9B4DBA;
        border: 2px solid #FFB6DC;
        border-radius: 15px;
        padding: 0.6rem 1rem;
        font-weight: 400;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        text-align: left;
        font-size: 0.9rem;
        box-shadow: 0 2px 8px rgba(255, 105, 180, 0.1);
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(90deg, #FFB6DC 0%, #D9A6FF 100%);
        color: white;
        border-color: #FF6FB5;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(255, 105, 180, 0.35);
    }

    /* Chat input box - glowing pink */
    .stChatInput > div {
        border-radius: 30px !important;
        border: 2px solid #FFB6DC !important;
        background: white !important;
        box-shadow: 0 5px 20px rgba(255, 105, 180, 0.2);
        transition: all 0.3s ease;
    }

    .stChatInput > div:focus-within {
        box-shadow: 0 5px 25px rgba(255, 105, 180, 0.45);
        border-color: #FF6FB5 !important;
    }

    .stChatInput textarea {
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.95rem !important;
    }

    /* Clear conversation button (last sidebar button) */
    section[data-testid="stSidebar"] .stButton:last-of-type > button {
        background: linear-gradient(90deg, #FF8FB8 0%, #FF6FB5 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 12px rgba(255, 105, 180, 0.3);
    }

    section[data-testid="stSidebar"] .stButton:last-of-type > button:hover {
        background: linear-gradient(90deg, #FF6FB5 0%, #E0559C 100%);
        box-shadow: 0 6px 20px rgba(255, 105, 180, 0.5);
    }

    /* Divider color */
    hr {
        border-color: rgba(255, 182, 220, 0.5) !important;
    }

    /* Caption text */
    .stCaption {
        color: #B07CC4 !important;
        font-size: 0.8rem !important;
        text-align: center;
    }

    /* Spinner color */
    .stSpinner > div {
        border-top-color: #FF6FB5 !important;
    }

    /* Hide Streamlit default menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------
# Header
# ------------------------------------------
st.markdown('<div class="main-header">🌸 Rubi AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">✨ Your Personal Assistant — Ask me about Rubab Fatima ✨</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="divider-hearts">💗 ─── ✨ ─── 💗</div>', unsafe_allow_html=True)


# ------------------------------------------
# Sidebar
# ------------------------------------------
with st.sidebar:
    st.markdown("### 💖 About Me")
    st.write(
        "**Rubi AI** is a RAG-based chatbot that answers questions "
        "about Rubab Fatima using her personal CV and documents."
    )
    st.divider()

    st.markdown("### 💭 Sample Questions")
    sample_questions = [
        "What is Rubab's email address?",
        "What projects has Rubab worked on?",
        "What are her digital skills?",
        "What is her education?",
        "Tell me about her Shopify store.",
    ]
    for q in sample_questions:
        if st.button(q, use_container_width=True):
            st.session_state.pending_question = q

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        if "bot" in st.session_state:
            st.session_state.bot.reset()
        st.rerun()

    st.divider()
    st.caption("💗 Built with LangChain, FAISS, Groq & Streamlit")


# ------------------------------------------
# Initialize Session State
# ------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "bot" not in st.session_state:
    with st.spinner("Loading Rubi AI..."):
        st.session_state.bot = RubiAIChatbot()

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


# ------------------------------------------
# Display Chat History
# ------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(
        message["role"],
        avatar="👩" if message["role"] == "user" else "🌸"
    ):
        st.markdown(message["content"])


# ------------------------------------------
# Handle Sample Question Click
# ------------------------------------------
if st.session_state.pending_question:
    user_input = st.session_state.pending_question
    st.session_state.pending_question = None

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👩"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🌸"):
        with st.spinner("Thinking..."):
            response = st.session_state.bot.respond(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()


# ------------------------------------------
# Chat Input
# ------------------------------------------
user_input = st.chat_input("💬 Ask me anything about Rubab...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👩"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🌸"):
        with st.spinner("Thinking..."):
            response = st.session_state.bot.respond(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})


# ------------------------------------------
# Footer
# ------------------------------------------
st.divider()
st.caption("💗 Rubi AI answers only from Rubab's personal data. She will not make up information.")