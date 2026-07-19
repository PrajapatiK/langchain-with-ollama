# 🤖 Streamlit AI Chatbot with LangChain, Ollama & LangSmith

A conversational AI chatbot built with **Streamlit**, **LangChain**, **Ollama**, and **SQLite**. The application supports real-time streaming responses, persistent chat history, multiple user sessions, and optional LangSmith tracing for debugging and monitoring.

---

## ✨ Features

* 💬 Interactive chat interface using Streamlit
* 🤖 Local LLM powered by Ollama
* ⚡ Real-time streaming responses
* 📝 Persistent chat history using SQLite
* 👤 Multiple user sessions
* 🔄 Start a new conversation anytime
* 📊 Optional LangSmith tracing for monitoring and debugging
* 🔗 Built using LangChain Expression Language (LCEL)

---

## 🛠️ Tech Stack

* Python 3.12+
* Streamlit
* LangChain
* LangChain Ollama
* Ollama
* SQLite
* SQLAlchemy
* python-dotenv
* LangSmith (Optional)

---

## 📁 Project Structure

```text
chatbot/
│
├── chat_stream.py          # Main Streamlit application
├── chat_history.db         # SQLite database (created automatically)
├── .env                    # Environment variables
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Prerequisites

Before running the project, install the following:

* Python 3.12 or later
* Ollama

Download Ollama from:

https://ollama.com/download

---

# Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git

cd <your-repository>
```

---

# Step 2: Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

# Step 3: Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet:

```bash
pip install streamlit langchain langchain-core langchain-community langchain-ollama python-dotenv sqlalchemy ollama
```

---

# Step 4: Configure Environment Variables

Create a `.env` file in the project root.

```env
# -----------------------------
# LangSmith Configuration (Optional)
# -----------------------------

LANGCHAIN_API_KEY="your_langsmith_api_key"
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="streamlit-chatbot"

# -----------------------------
# Future API Keys (Optional)
# -----------------------------

# OPENAI_API_KEY=""
# GOOGLE_API_KEY=""
# ANTHROPIC_API_KEY=""
```

### Environment Variable Description

| Variable               | Description                                    |
| ---------------------- | ---------------------------------------------- |
| `LANGCHAIN_API_KEY`    | Your LangSmith API key.                        |
| `LANGCHAIN_TRACING_V2` | Enables LangSmith tracing (`true` or `false`). |
| `LANGCHAIN_ENDPOINT`   | LangSmith API endpoint.                        |
| `LANGCHAIN_PROJECT`    | Project name displayed in LangSmith.           |

> **Note:** LangSmith is optional. If you don't want tracing, either remove these variables or set `LANGCHAIN_TRACING_V2=false`.

---

# Step 5: Install the Ollama Model

Download the Llama model:

```bash
ollama pull llama3.2
```

Verify the installed models:

```bash
ollama list
```

Example output:

```text
NAME
llama3.2:latest
```

If your installed model name differs, update the `model` variable in `chat_stream.py` accordingly.

Example:

```python
model = "llama3.2"
```

or

```python
model = "llama3.2:latest"
```

---

# Step 6: Start the Ollama Server

Run:

```bash
ollama serve
```

The default endpoint is:

```text
http://localhost:11434
```

---

# Step 7: Run the Streamlit Application

Start the chatbot:

```bash
streamlit run chat_stream.py
```

The application will open in your browser:

```text
http://localhost:8501
```

---

# 🚀 How to Use

1. Enter a unique **User ID**.
2. Type your question in the chat input.
3. Receive AI-generated responses in real time.
4. All conversations are automatically stored in SQLite.
5. Click **Start New Conversation** to clear the current session history.

---

# 💾 Chat History

The application stores conversations in:

```text
chat_history.db
```

Each **User ID** maintains its own conversation history.

---

# 📊 LangSmith Tracing (Optional)

This project supports **LangSmith** for debugging and monitoring.

With LangSmith you can:

* View prompts and responses
* Inspect execution flow
* Monitor latency and token usage
* Debug LangChain chains
* Analyze conversation history

To enable tracing:

1. Create a LangSmith account.
2. Generate an API key.
3. Add it to the `.env` file.
4. Restart the Streamlit application.

---

# 📦 Dependencies

```text
streamlit
langchain
langchain-core
langchain-community
langchain-ollama
ollama
python-dotenv
sqlalchemy
```

Generate a `requirements.txt` file anytime with:

```bash
pip freeze > requirements.txt
```

---

# 🐞 Troubleshooting

## Model not found

```text
ollama._types.ResponseError:
model 'llama3.2' not found
```

**Solution**

```bash
ollama pull llama3.2
```

Check installed models:

```bash
ollama list
```

---

## Ollama connection refused

Start the Ollama server:

```bash
ollama serve
```

---

## Port 11434 not reachable

Verify Ollama is running:

```bash
curl http://localhost:11434
```

---

## SQLite database issues

Delete the existing database:

```bash
rm chat_history.db
```

It will be recreated automatically on the next run.

---

## Missing Python packages

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Enhancements

* Retrieval-Augmented Generation (RAG)
* PDF Chat
* Document Upload
* Authentication & Authorization
* Vector Database (ChromaDB / FAISS)
* Multi-LLM Support
* Docker Support
* Chat Export (PDF/Markdown)
* Conversation Analytics

---

# 📄 License

This project is open for learning and experimentation. Feel free to fork, modify, and enhance it.

If you find this project useful, consider giving it a ⭐ on GitHub.
