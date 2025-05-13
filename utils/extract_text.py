import fitz  # PyMuPDF

def extract_text(file_path):
    text = ''
    if file_path.endswith('.pdf'):
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    return text
