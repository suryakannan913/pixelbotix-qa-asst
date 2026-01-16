import os
from ingest import ingest_pdf
from chat import answer_question

# Set the PDF path
pdf_filename = "dmv.pdf"  # EXACT file name
pdf_path = os.path.join("docs", pdf_filename)  # Windows-safe path

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF not found at {pdf_path}")

# Ingest the PDF
print(f"Ingesting PDF immediately: {pdf_path} ...")
ingest_pdf(pdf_path)
print("PDF ingested and FAISS index saved .\n")

while True:
    q = input("Ask a question: ")
    answer, sources = answer_question(q)
    print("\nAnswer:", answer)
    print("Sources:", sources)