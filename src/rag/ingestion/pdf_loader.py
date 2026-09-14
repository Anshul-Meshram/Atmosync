import fitz
from pathlib import Path


def extract_pages_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extract text from a PDF while preserving page information.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of dictionaries containing page number and page text.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, got: {pdf_path.suffix}")

    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text().strip()

        pages.append({
            "page": page_number,
            "text": text
        })

    document.close()

    return pages


def check_pdf_text(pages: list[dict]) -> bool:
    """
    Check whether the PDF contains extractable text.

    Returns:
        True if sufficient text is available, otherwise False.
    """

    total_characters = sum(len(page["text"]) for page in pages)

    if total_characters == 0:
        return False

    return True


if __name__ == "__main__":

    pdf_file = "M:/sem7/Major Project/AtmoSync/src/rag/documents/Climate_Intelligence_System_Project_Report.pdf"

    pages = extract_pages_from_pdf(pdf_file)

    has_text = check_pdf_text(pages)

    if not has_text:
        print("WARNING: No extractable text found.")
        print("This may be a scanned/image-based PDF.")
    else:
        print("PDF contains extractable text.")

    print(f"Total pages: {len(pages)}")
    print(
        f"Total characters: "
        f"{sum(len(page['text']) for page in pages)}"
    )