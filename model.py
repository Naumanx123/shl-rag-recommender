import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def load_data_and_index():
    df = pd.read_csv("app/data/shl_assessments.csv")
    df["duration"] = df["duration"].fillna(30).astype(int)
    df["test_type"] = df["test_type"].fillna("").astype(str)
    df["text"] = df.apply(lambda row: f"{row['name']} test_type: {row['test_type']} duration: {row['duration']}min remote_testing: {row['remote_testing']} adaptive_irt: {row['adaptive_irt']}", axis=1)

    texts = df["text"].tolist()
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(texts)

    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return df.to_dict(orient="records"), model, index

def get_recommendations(query, model, index, products, top_k=5):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [products[i] for i in I[0]]
