import fitz
import re

def extract_resume_text(pdf_file):

    text = ""

    doc = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in doc:
        text += page.get_text()

    text = re.sub(r"\s+", " ", text)

    return text.strip()