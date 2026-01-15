from lib.embeddings import embed_query
from lib.vector_store import load_index, search
from lib.prompts import build_qa_prompt
from lib.llm import generate_answer

def answer_question(question):
    index, metadata = load_index(
        "data/index.faiss",
        "data/metadata.pkl"
    )

    query_embedding = embed_query(question)
    top_indices = search(index, query_embedding)

    context_chunks = [metadata[i] for i in top_indices]

    prompt = build_qa_prompt(context_chunks, question)
    answer = generate_answer(prompt)

    sources = sorted(set(c["page"] for c in context_chunks))

    return answer, sources
