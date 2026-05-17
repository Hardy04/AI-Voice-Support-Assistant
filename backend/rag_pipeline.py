from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


with open("data/knowledge_base.txt", "r", encoding="utf-8") as file:
    documents = file.readlines()

embeddings = embedding_model.encode(documents)

index = faiss.IndexFlatL2(384)
index.add(np.array(embeddings, dtype=np.float32))


def retrieve_context(query: str):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(
        np.array(query_embedding, dtype=np.float32),
        3
    )

    retrieved_docs = [documents[idx] for idx in indices[0]]

    return "\n".join(retrieved_docs)
