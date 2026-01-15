import os
from lib.pdf_loader import load_pdf
from lib.chunking import chunk_pages
from lib.embeddings import embed_texts
from lib.vector_store import create_index, save_index

def ingest_pdf(file_path):
    pages = load_pdf(file_path)
    chunks = chunk_pages(pages)

    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)

    index = create_index(embeddings)

    # Ensure 'data/' folder exists
    os.makedirs("data", exist_ok=True)

    save_index(
        index,
        chunks,
        "data/index.faiss",
        "data/metadata.pkl"
    )
