from .retriever import retrieve_chunks

def main():
    print("="*60)
    print("RETRIEVAL TEST.")
    print("="*60)

    query = "What is the weather forecast for tomorrow in Toronto?"

    print(f"\nQuery: {query}\n")
    print("Searching for the query.....")

    results = retrieve_chunks(query, top_k =3)

    print(f"\nRetrieved {len(results)} chunks.\n")

    for index , result in enumerate(results,start = 1):
        print("\n"+"-"*60)
        print(f"Result {index}")
        print("-"*60)

        print(f"Score: {result['score']:.4f}")
        print(f"ChunkID: {result['chunk_id']}")
        print(f"Page :{result['page']}")
        print(f"Characters: {result['char_count']}")

        print("\nText:")
        print(result["text"][:500])

        if len(result["text"])>500:
            print("....... ")
    print("\n"+"="*60)
    print("RETRIEVAL TEST COMPLETED.")
    print("="*60)
if __name__ == "__main__":
    main()