import PyPDF2

# Конвертация PDF в текст
def convert_pdf_to_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text


text_from_pdf = convert_pdf_to_text("inst.pdf")
print(text_from_pdf)