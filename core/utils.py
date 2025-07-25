import os
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()
# -----------------------------
# Load environment variables
# -----------------------------
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_db")
VECTOR_DB_TYPE = os.getenv("VECTOR_DB_TYPE", "faiss")
_model = model = "mistralai/Mistral-7B-Instruct-v0.1"


# -----------------------------
# Embedding Functions
# -----------------------------

def embed_documents(docs: list[str]) -> list[list[float]]:
    """
    Embed a list of text documents using a local SentenceTransformer model.
    Returns a list of vector representations.
    """
    return _model.encode(docs, convert_to_numpy=True).tolist()


# -----------------------------
# Retrieval Agent
# -----------------------------

def retrieve_relevant_chunks(query: str, docs: list[str], top_k: int = 3) -> list[str]:
    """
    Given a query and list of document chunks, retrieve the most relevant ones.
    """
    if not docs:
        return []

    query_vec = embed_documents([query])[0]
    doc_vecs = embed_documents(docs)

    scores = cosine_similarity([query_vec], doc_vecs)[0]
    top_indices = scores.argsort()[-top_k:][::-1]

    return [docs[i] for i in top_indices]


# -----------------------------
# Response Generator
# -----------------------------
def generate_response(prompt: str) -> str:
    """
    Generate a response from a Hugging Face hosted LLM using API token from config.json.
    """
    model = "HuggingFaceH4/zephyr-7b-beta"
    api_url = f"https://api-inference.huggingface.co/models/{model}"

    try:
        # Load token from config.json
        with open("config.json", "r") as f:
            config = json.load(f)
        token = config.get("hf_api_token")
        if not token:
            raise ValueError("Missing 'hf_api_token' in config.json")

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 256,
                "temperature": 0.7,
                "return_full_text": False
            }
        }

        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        output = response.json()
        return output[0]["generated_text"]

    except Exception as e:
        print(f"❌ Hugging Face LLM Error: {e}")
        print(f"📨 Response: {response.text if 'response' in locals() else 'No response'}")
        return "⚠️ LLM failed to generate a response."
import requests 
