import faiss
import numpy as np
import pickle

def create_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)
    return index


def save_index(index, metadata, index_path, meta_path):
    faiss.write_index(index, index_path)
    with open(meta_path, "wb") as f:
        pickle.dump(metadata, f)


def load_index(index_path, meta_path):
    index = faiss.read_index(index_path)
    with open(meta_path, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata


def search(index, query_embedding, k=4):
    vector = np.array([query_embedding]).astype("float32")
    _, indices = index.search(vector, k)
    return indices[0]
