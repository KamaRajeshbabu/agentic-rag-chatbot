# 🤖 Agentic RAG Chatbot

> An open-source, **modular Retrieval-Augmented Generation (RAG) chatbot** powered by Hugging Face Transformers and LangChain.  
> **Secure, extendable, and production-ready AI assistant.**

![Banner](<img width="1536" height="1024" alt="generated-image" src="https://github.com/user-attachments/assets/7c845f6c-f70c-4651-a3c8-479daf225eb0" />)


## 🚀 Why This Project?

Most chatbots are just wrappers over LLM APIs.  
**Agentic RAG Chatbot is different:**

- 🧩 **Agentic reasoning** (tasks, tools, planning)
- 📖 **RAG** (retrieval from docs & web)
- 🔒 **Secure config management**
- 🛠️ **Modular, production-ready codebase**

Build real AI tools with confidence.

## 🧠 Core Features

- ✅ **Agentic LLM Behavior**  
  Modular agent using LangChain-style tool invocation and chaining.
- ✅ **Retrieval-Augmented Generation**  
  Fetch documents, web, or API data – answers grounded in facts.
- ✅ **Clean Structure**  
  Isolated `utils/` for embedding, LLM, scraping, text processing.
- ✅ **Secure**  
  `.env` in `.gitignore`, secrets protected — safe for sharing and deployment.
- ✅ **Hackable**  
  Clear, concise code. Easy to extend and customize. No bloat.

## 📁 Project Structure

```text
├── config.json
├── requirements.txt
├── retrieval_agent.py
├── test_hf_model.py
└── utils/
    ├── embedding_utils.py
    ├── file_utils.py
    ├── llm_utils.py
    ├── retrieval_utils.py
    ├── scraper_utils.py
    └── text_utils.py
```

## ⚙️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/KamaRajeshbabu/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```

### 2. Setup Environment

```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### 3. Set Your `.env`

Create a `.env` file with your Hugging Face / OpenAI keys:

```env
HF_API_KEY=your_key
OPENAI_API_KEY=your_key
```

### 4. Run the Agent

```bash
python retrieval_agent.py
```

## 🧪 Run Tests

Test your model setup:

```bash
python test_hf_model.py
```



⚡ **Enjoy building secure, modular, production-ready RAG chatbots!** 🚀

