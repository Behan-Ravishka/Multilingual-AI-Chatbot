# 🌍 Multilingual Local AI Chatbot

A highly responsive, multilingual conversational AI assistant built entirely with local, open-weights machine learning models. This application ensures complete data privacy by running inference locally without relying on external APIs.

## 📸 Project Screenshots
*(Replace the file names below with your actual screenshot names)*
![Chat Interface](assets/screenshot1.png)
![Language Switching](assets/screenshot2.png)
![Backend Loading](assets/screenshot3.png)

## 🛠️ Technology Stack & Architecture

This project was built using the following technologies, specifically chosen for a lightweight, local-first execution pipeline:

*   **Python (3.12):** The core programming language managing the application logic and backend processes.
*   **Streamlit:** A rapid-prototyping framework used to build the interactive, reactive frontend user interface (UI) directly from Python code.
*   **Ollama:** A local inference engine that serves large language models (LLMs) on standard hardware. It manages memory allocation and model execution, acting as the bridge between the Python app and the AI model.
*   **LLaMA 3.2 (1B):** The foundational Large Language Model powering the chat. The 1-Billion parameter version was specifically selected for its low-overhead requirements, allowing smooth inference on an i3 CPU with 12GB RAM.
*   **Jupyter Notebook:** Used for initial scripting, environment testing, and step-by-step code execution before exporting to the final Streamlit application.

## 🧠 Core Concepts for Revision

### How the Local AI Pipeline Works:
1.  **User Input:** The user types a prompt into the Streamlit web interface.
2.  **API Bridge:** The Python script uses the `ollama` library to package the prompt and send a local HTTP request to the Ollama server running in the background.
3.  **Inference Execution:** Ollama processes the prompt through the LLaMA 3.2 model weights.
4.  **Streaming Response:** The generated tokens are streamed back to the Streamlit UI in real-time, creating a smooth conversational experience.

### Why Virtual Environments (`.venv`) Matter:
This project utilizes an isolated `.venv` to prevent dependency conflicts (e.g., NumPy and PyArrow binary mismatches) with system-wide Python packages.

## 🚀 Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/Multilingual-AI-Chatbot.git](https://github.com/yourusername/Multilingual-AI-Chatbot.git)
cd Multilingual-AI-Chatbot
```

**2. Activate the Virtual Environment**
Ensure you are running Python 3.12.
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install streamlit ollama
```

**4. Run the Application**
Ensure the Ollama engine is running in the background, then launch the frontend:
```bash
streamlit run app.py
```
