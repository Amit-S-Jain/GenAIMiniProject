import fitz

def extract_text(pdf_path: str) -> str:
    text = ""

    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()

    return text

if __name__ == "__main__":
    pdf_text = "C:/Users/amits/Desktop/GenAi/NaukriAI/parser/resume2.pdf"
    resume_text = extract_text(pdf_text)
    print(resume_text)