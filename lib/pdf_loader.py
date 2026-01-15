import fitz  # PyMuPDF

def load_pdf(file_path: str):
    doc = fitz.open(file_path)
    pages = []

    for num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if text.strip():
            pages.append({"page": num, "text": text.strip()})

    return pages

