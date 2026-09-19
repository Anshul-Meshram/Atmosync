import uuid

from qdrant_client.models import PointStruct 
from src.rag.embeddings.embedding_model import generate_embedding
from src.rag.vector_db.qdrant_client import client, COLLECTION_NAME

def index_chunks(chunks: list[dict]) -> int:
    """
    Generate embeddings for chunks and store them in Qdrant.

    Args:
        chunks: List of chunk dictonaries produced by the chunking pipeline.
    
    Returns:
        Number of chunks successfully indexed .
    """
    points = []

    for chunk in chunks:
        text = chunk["text"].strip()\

        # Skip empty chunks :
        if not text :
            continue

        # Generate embedding
        vector = generate_embedding(text)

        # Create a stable point ID
        point_id = str(
            uuid.uuid5(
                uuid.NAMESPACE_URL,
                chunk["chunk_id"]
                )
            )

        # Create Qdrant Point 
        point = PointStruct(
            id=point_id,
            vector=vector,
            payload={
                "chunk_id": chunk["chunk_id"],
                "page": chunk["page"],
                "text": text,
                "char_count": chunk["char_count"],
            },
        )
        points.append(point)

        #Upload points to Qdrant
        if points:
            client.upsert(
                collection_name = COLLECTION_NAME,
                points = points,
                wait = True,
                )
    return len(points)
    