from docling.document_converter import DocumentConverter
def resume_reader_txt(resume_path):
    print("Inside Docling", resume_path)
    converter = DocumentConverter()

    result = converter.convert(resume_path)

    resume_markdown = result.document.export_to_markdown()

    print("Resume Docling result")
    print(resume_markdown)
    return resume_markdown


if __name__ == "__main__":
    resume_text = resume_reader_txt("C:/Users/amits/Desktop/GenAi/NaukriAI/parser/resume2.pdf")
    print(resume_text)