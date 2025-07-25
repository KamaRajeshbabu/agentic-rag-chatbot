import os
from agents.ingestion_agent import ingest_files
from core.utils import retrieve_relevant_chunks, generate_response
from core.parsers import parse_pdf, parse_docx, parse_csv, parse_pptx, parse_txt
from dotenv import load_dotenv
import requests

def answer_query(query: str, docs: list[str]) -> str:
    relevant_chunks = retrieve_relevant_chunks(query, docs)
    if not relevant_chunks:
        return "⚠️ No relevant information found."

    context = "\n\n".join(relevant_chunks)
    prompt = f"Based on the following context, answer the question:\n\n{context}\n\nQuestion: {query}"
    return generate_response(prompt)

if __name__ == "__main__":
    print("🚀 Starting Agentic RAG Chatbot (Huggingface Mode)")

    files = os.listdir("data")
    print(f"\n📂 Files in /data: {files}")
    selected_files = input("Enter filenames to parse (comma-separated): ").strip().split(",")

    selected_files = [f.strip() for f in selected_files if f.strip()]
    user_query = input("\n🔍 Enter your question: ").strip()

    print("\n🔄 Flow: User → IngestionAgent → RetrievalAgent → LLMResponseAgent")

    parsed_chunks = ingest_files(selected_files)
    answer = answer_query(user_query, parsed_chunks)

    print(f"\n🧠 Final Answer:\n{answer}")
 
