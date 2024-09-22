import pdfplumber

def analyze_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Simple example of extracting key values (e.g., cholesterol, glucose levels)
    cholesterol = extract_value(text, 'Cholesterol')
    glucose = extract_value(text, 'Glucose')

    return {
        "Cholesterol": cholesterol,
        "Glucose": glucose
    }

def extract_value(text, key):
    # Simple text parsing to extract a health marker (replace with more robust methods)
    if key in text:
        start_idx = text.find(key) + len(key)
        value = text[start_idx:start_idx+10].strip()
        return value
    return "Not found"
