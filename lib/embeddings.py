from google import genai
import numpy as np
import os

from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def embed_texts(chunks):
    """
    Embed multiple text chunks using Gemini embeddings.
    Returns a NumPy array of shape (num_chunks, embedding_dim)
    """
    embeddings = []
    try:
        for chunk in chunks:
            result = client.models.embed_content(
                model='models/text-embedding-004',
                contents=chunk
            )
            # .values is the correct property in Gemini SDK
            embeddings.append(result.embeddings[0].values)
        return np.array(embeddings, dtype=np.float32)
    except Exception as e:
        st.error(f"Error creating embeddings: {str(e)}")
        return None

def embed_query(query):
    """
    Embed a single query string using Gemini embeddings.
    Returns a NumPy array of shape (embedding_dim,)
    """
    try:
        result = client.models.embed_content(
            model='models/text-embedding-004',
            contents=[query]
        )
        return np.array(result.embeddings[0].values, dtype=np.float32)
    except Exception as e:
        st.error(f"Error embedding query: {str(e)}")
        return None