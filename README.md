# 🤖 Agentic RAG Chatbot

> An open-source, modular Retrieval-Augmented Generation (RAG) chatbot powered by Hugging Face Transformers and LangChain. Designed for secure, extendable, and production-ready AI assistants.

---

## 🚀 Why This Project Exists

Most chatbots are just wrappers over LLM APIs. This one’s different.

Agentic RAG Chatbot combines:
- **Agentic reasoning** (tasks, tools, planning)
- **RAG** (retrieval from context-aware sources)
- **Secure config management**
- A modular, production-ready codebase you can build real tools on.

---

## 🧠 Core Features

✅ **Agentic LLM Behavior**  
Modular agent that uses LangChain-style tool invocation and chaining logic.

✅ **Retrieval-Augmented Generation**  
Fetches data from documents, web sources, or APIs to ground LLM answers in facts.

✅ **Clean Structure**  
Split into isolated `utils/` for embedding, LLM, scraping, text processing.

✅ **Secure**  
Git-ignored `.env`, secrets excluded, safe to deploy or share.

✅ **Hackable**  
Clear code. Easy to extend. No bloated architecture or overengineering.

---

## 📁 Project Structure
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


