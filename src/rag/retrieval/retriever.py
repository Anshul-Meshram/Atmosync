from src.rag.embeddings.embedding_model import generate_embedding
from src.rag.vector_db.qdrant_client import client, COLLECTION_NAME

def retrieve_chunks(query:str, top_k: int = 5)->list[dict]:
    """
    Retrieves the most relevant chunks from Qdrant.

    Args:
        query: User's natural-language question.
        top_k: Number of relevant chunks to retrieve.

    Returns:
        List of retrieved chunks with similarity scores.
    """
    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    # Generate embedding for the user's query.
    query_vector = generate_embedding(query.strip())

    # Search Qdrant 
    search_results = client.query_points(
        collection_name = COLLECTION_NAME,
        query = query_vector,
        limit = top_k,
        with_payload = True,
        with_vectors = False,
    ).points

    results = []

    for result in search_results:
        payload = result.payload or {}

        results.append(
            {
                "score": result.score,
                "chunk_id": payload.get("chunk_id"),
                "page": payload.get("page"),
                "text": payload.get("text"),
                "char_count": payload.get("char_count"),
            }
        )
    return results
