# utils/embedding_utils.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self):
        self.texts = []
        self.index = faiss.IndexFlatL2(384)

    def add(self, texts):
        embeddings = model.encode(texts)
        self.index.add(np.array(embeddings))
        self.texts.extend(texts)

    def search(self, query, k=3):
        embedding = model.encode([query])
        scores, ids = self.index.search(np.array(embedding), k)
        return [self.texts[i] for i in ids[0]]
