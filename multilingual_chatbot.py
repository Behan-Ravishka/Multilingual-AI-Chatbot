

import streamlit as st
import ollama

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Multilingual AI Assistant",
    page_icon="🌍",
    layout="centered"
)

# =====================================
# CSS STYLING
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #f0f2f5;
}

.user-bubble {
    background-color: #dcf8c6;
    color: black;
    padding: 10px;
    border-radius: 15px;
    margin-bottom: 10px;
}

.bot-bubble {
    background-color: white;
    color: black;
    padding: 10px;
    border-radius: 15px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SYSTEM PROMPT
# =====================================

SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are a highly accurate multilingual AI assistant for Sri Lanka.

Rules:
1. Detect the user's language automatically.
2. If the user writes in Sinhala, reply only in Sinhala.
3. If the user writes in Tamil, reply only in Tamil.
4. If the user writes in English, reply only in English.
5. Never mix languages unless the user mixes them.
6. If unsure, clearly say you do not know.
7. Never hallucinate or invent facts.
8. Keep responses short, accurate, and helpful.
"""
}

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.success("🟢 Ollama Connected")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = [SYSTEM_PROMPT]
        st.rerun()

# =====================================
# CHAT MEMORY
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

# =====================================
# TITLES
# =====================================

st.markdown(
    "<h2 style='text-align:center;'>🌍 Multilingual Offline Chatbot</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Powered by Ollama + Llama 3.2:1b</p>",
    unsafe_allow_html=True
)

# =====================================
# DISPLAY CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"<div class='user-bubble'>{message['content']}</div>",
            unsafe_allow_html=True
        )

    elif message["role"] == "assistant":

        st.markdown(
            f"<div class='bot-bubble'>{message['content']}</div>",
            unsafe_allow_html=True
        )

# =====================================
# USER INPUT
# =====================================

prompt = st.chat_input("Type your message")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.rerun()

# =====================================
# GENERATE RESPONSE
# =====================================

if st.session_state.messages[-1]["role"] == "user":

    with st.spinner("Thinking..."):

        try:

            response = ollama.chat(
                model="llama3.2:1b",
                messages=st.session_state.messages,
                keep_alive=-1,
                options={
                    "temperature": 0.2,
                    "num_ctx": 4096,
                    "num_predict": 256
                }
            )

            answer = response["message"]["content"]

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            st.rerun()

        except Exception as e:

            st.error("Could not connect to Ollama.")

