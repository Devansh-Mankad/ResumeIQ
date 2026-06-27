import fitz


def extract_resume_text(pdf_file):
    """
    Extract all text from an uploaded PDF resume.
    Parameters
    ----------
    pdf_file : FileStorage
        Uploaded PDF file received from Flask.
    Returns
    -------
    str
        Complete extracted text from the PDF.
    """
    
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in document:
        text += page.get_text()
        text += "\n"
    document.close()

    return text.strip()