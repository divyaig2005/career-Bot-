import os
import streamlit as st
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY and "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

if not GEMINI_API_KEY:
    st.error("❌ API Key not found. Please check .env file or Streamlit secrets.")
    st.stop()

# ========== CONFIGURE YOUR GEMINI API KEY ==========
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# ========== GET CAREER ADVICE FUNCTION ==========
def get_career_guidance(user_input: str) -> str:
    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""
    You are a specialized AI assistant that ONLY provides detailed career guidance.

    When the user's input is related to career guidance (e.g., skills, interests, education for job suggestions), analyze their profile and suggest 10 suitable, future-proof career options. Be supportive, insightful, and motivational.

    Each career suggestion must include:
    - A bold career title
    - A 1-2 line description of why it's a good fit
    - A clickable and trusted resource link using [text](URL) format

    Add a closing line: "🌟 You've got this! Explore what excites you and build a future you love."

    User Input:
    {user_input}

    Response format for career guidance:
    1. **Career Title**
       Description
       🔗 [Link Text](URL)

    2. ...
    3. ...
    ...
    10. ...
    """

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return "✅ Got response but couldn't parse it properly."
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# ========== STREAMLIT UI CONFIG ==========
st.set_page_config(page_title="Career Guidance Chatbot", page_icon="🎯")

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
.stChatInput textarea {
    border-color: green !important;
}
</style>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("🧭 About This App")
    st.info("This AI-powered chatbot helps you explore personalized career paths based on your skills, interests, and education.")
    st.markdown("""
    **Why This App?**
    - Personalized AI career suggestions.
    - Up to 10 options with links.
    - Powered by Gemini for accuracy.
    - Unique for career guidance.
    """)
    st.markdown("🔗 Powered by [Gemini API](https://aistudio.google.com/)")

# ========== MAIN INTERFACE ==========
st.title("🎯 Career Guidance Chatbot")
st.markdown("Describe your **skills**, **interests**, and **education background**. Get personalized and practical career suggestions.")

# ========== SESSION STATE ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========== DISPLAY CHAT HISTORY ==========
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# ========== CHAT INPUT ==========
if prompt := st.chat_input("Describe your skills, interests, and education background..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Brewing career magic... ✨"):
            response = get_career_guidance(prompt)
            st.markdown(response, unsafe_allow_html=True)
        st.caption("Powered by Gemini API")
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# ========== FOOTER ==========
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("💡 Tip: Ask again with different skills or interests to explore more career paths.")
st.markdown("### 🌟 Unleash Your Career Potential with AI Magic! 🌟")
st.caption("Crafted with ❤️ for dreamers and achievers.")
