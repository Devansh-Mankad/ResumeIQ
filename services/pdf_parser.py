import fitz

def extract_resume_text(pdf_path):
    """
    Extract all text from a PDF resume.
    Parameters
    ----------
    pdf_path : str
        Path of uploaded PDF.

    Returns
    -------
    str
        Complete extracted text.
    """

    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        page_text = page.get_text()
        if page_text:
            text += page_text
            text += "\n"
    document.close()
    return text.strip()