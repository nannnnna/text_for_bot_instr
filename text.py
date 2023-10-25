import PyPDF2

# Конвертация PDF в текст
def convert_pdf_to_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        texts = []
        for page in range(len(reader.pages)):
            texts.append(reader.pages[page].extract_text())
    return texts

texts_from_pdf = convert_pdf_to_text("inst.pdf")
print(texts_from_pdf)
# for page_num, text in enumerate(texts_from_pdf, 1): вывод всего текста с допоплнительной нумерацией страниц
#     print(f"------ Page {page_num} ------")
#     print(text)
#     print("-----------------------------\n")