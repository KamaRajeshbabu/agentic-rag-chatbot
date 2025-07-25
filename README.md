# Agentic RAG Chatbot

A Retrieval-Augmented Generation chatbot using an agent-based architecture and Model Context Protocol (MCP) for document-based question answering.

## 🧠 Architecture

- IngestionAgent: Parses documents (PDF, DOCX, CSV, etc.)
- RetrievalAgent: Embeds + retrieves relevant chunks from vector store
- LLMResponseAgent: Forms prompt and gets answer from LLM
- MCP: Used to pass structured messages between agents

## 🖼️ UI

Built using Streamlit. Allows multi-format upload + Q&A.

## ⚙️ Stack

- Python, Streamlit
- Sentence Transformers (MiniLM)
- FAISS
- Hugging Face LLMs (Falcon 7B)
- MCP for message flow

## 📦 Setup

```bash
pip install -r requirements.txt
streamlit run app.py
