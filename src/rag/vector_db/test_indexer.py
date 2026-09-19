from src.rag.ingestion.pdf_loader import process_pdf
from src.rag.ingestion.chunker import chunk_pages
from src.rag.vector_db.indexer import index_chunks
print("IMPORT completed successfully")
PDF_PATH = "M:/sem7/Major Project/AtmoSync/src/rag/documents/Climate_Intelligence_System_Project_Report.pdf"

def main():
    print("="*60)
    print("QDRANT INDEXING TEST.")
    print("="*60)

    print("\n1. Loading PDF........")
    pages = process_pdf(PDF_PATH)

    print(f"Pages loaded : {len(pages)}")

    print("\n2. Creating chunks.......")
    chunks = chunk_pages(pages)

    print(f"Total chunks created: {len(chunks)}")

    print("\n3. Generating embeddings and indexing into Qdrant.....")
    count = index_chunks(chunks)

    print(f"Chunks indexed: {count}")

    print("\n" + "="*60)
    print("INDEXING COMPLETED")
    print("="*60)

if __name__ == "__main__":
    main()