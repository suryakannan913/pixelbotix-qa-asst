import re

def semantic_chunk_text(text, max_tokens=1000):
    """
    Split text into sentence-like chunks using simple punctuation rules,
    then combine sentences into chunks <= max_tokens.
    """
    # Simple sentence split: split on .!? followed by space or newline
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_chunk = ""
    token_count = 0

    for sent in sentences:
        sent_tokens = len(sent.split())
        if token_count + sent_tokens > max_tokens:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sent
            token_count = sent_tokens
        else:
            if current_chunk:
                current_chunk += " " + sent
            else:
                current_chunk = sent
            token_count += sent_tokens

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def chunk_pages(pages, max_tokens=500):
    all_chunks = []
    for page in pages:
        chunks = semantic_chunk_text(page["text"], max_tokens=max_tokens)
        for c in chunks:
            all_chunks.append({"page": page["page"], "text": c})
    return all_chunks

