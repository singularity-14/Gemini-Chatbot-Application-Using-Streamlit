# 🤖 Gemini Pro Q&A Chatbot

> An interactive question-answering chatbot powered by Google Gemini Pro — featuring real-time streaming responses and persistent chat history, built with Streamlit.

---

## 📌 Project Overview

This project demonstrates direct integration with **Google's Gemini Pro** generative AI model via the `google-generativeai` SDK. Users can ask any question and receive streamed, real-time responses — with the full conversation history displayed in-session.

A clean, minimal implementation that showcases **LLM API integration**, **streaming output handling**, and **stateful UI** design — foundational skills for any AI/ML engineer.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| ⚡ Streaming responses | Gemini replies stream chunk-by-chunk for real-time output |
| 🧠 Multi-turn chat | Uses `model.start_chat(history=[])` for stateful conversation |
| 📜 Chat history | Full Q&A history persisted in Streamlit session state |
| 🔐 Secure config | API key managed via `.env` and `python-dotenv` |
| 🖥️ Streamlit UI | Lightweight, interactive frontend with zero frontend code |

---

## 🚀 Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| LLM | Google Gemini Pro (`gemini-pro`) |
| SDK | `google-generativeai` |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## 🏗️ How It Works

```
User types a question → clicks "Ask Question to Gemini"
        ↓
google.generativeai SDK
  └── model: gemini-pro
  └── chat.send_message(question, stream=True)
        ↓
Streamed response chunks rendered live in UI
        ↓
Both question + response chunks saved to session state
        ↓
Full chat history displayed below the response
```

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
> Get your free API key at [aistudio.google.com](https://aistudio.google.com)

### 4. Run the app
```bash
streamlit run gemini.py
```
Visit `http://localhost:8501` in your browser.

---

## 🖥️ How to Use

1. Type your question in the **Input** field
2. Click **"Ask Question to Gemini"**
3. Watch the response stream in real time under **Response**
4. Review your full conversation under **History**

**Example:**
- Input: `"What is the capital of France?"`
- Response: `"The capital of France is Paris."`

---

## 📂 Project Structure

```
gemini-chatbot/
│
├── gemini.py           # Full application — Gemini SDK setup, streaming logic, Streamlit UI
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed to version control)
└── README.md           # Project documentation
```

---

## 💡 Key Learnings & Takeaways

- Integrated **Google Gemini Pro** directly via the `google-generativeai` SDK (no LangChain abstraction), building familiarity with the raw API
- Implemented **streaming response handling** — iterating over response chunks for real-time output rendering
- Used **Streamlit session state** to persist multi-turn chat history across reruns
- Understood the difference between **stateless** (single-turn) and **stateful** (multi-turn via `start_chat`) Gemini API usage

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*A foundational project exploring direct LLM API integration, streaming output, and stateful chat UI construction.*
