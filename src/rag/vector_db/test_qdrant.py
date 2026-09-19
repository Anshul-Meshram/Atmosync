from src.rag.vector_db.qdrant_client import client, COLLECTION_NAME


def main():
    print("=" * 60)
    print("QDRANT STORAGE VERIFICATION")
    print("=" * 60)

    # Check collection
    print("\n1. Checking collection...")

    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    if COLLECTION_NAME not in collection_names:
        print(f"ERROR: Collection '{COLLECTION_NAME}' not found.")
        return

    print(f"Collection '{COLLECTION_NAME}' exists.")

    # Get collection information
    print("\n2. Checking stored points...")

    collection_info = client.get_collection(
        collection_name=COLLECTION_NAME
    )

    print(f"Points stored: {collection_info.points_count}")

    if collection_info.points_count == 0:
        print("ERROR: Collection is empty.")
        return

    # Retrieve stored points
    print("\n3. Retrieving sample point...")

    points, next_page = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=1,
        with_payload=True,
        with_vectors=False,
    )

    if not points:
        print("ERROR: No points could be retrieved.")
        return

    point = points[0]

    print("\nSample point:")
    print("-" * 60)

    print(f"Point ID   : {point.id}")
    print(f"Chunk ID    : {point.payload.get('chunk_id')}")
    print(f"Page       : {point.payload.get('page')}")
    print(f"Char count : {point.payload.get('char_count')}")

    text = point.payload.get("text", "")

    print("\nText preview:")
    print(text[:500])

    if len(text) > 500:
        print("...")

    print("-" * 60)

    print("\n" + "=" * 60)
    print("QDRANT VERIFICATION COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()