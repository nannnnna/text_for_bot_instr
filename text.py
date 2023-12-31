import PyPDF2
import re

# Конвертация PDF в текст
def convert_pdf_to_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        texts = []
        for page in range(len(reader.pages)):
            texts.append(reader.pages[page].extract_text())
    return texts

texts_from_pdf = convert_pdf_to_text("inst.pdf")
# print(texts_from_pdf)

def convert_pdf_to_text_range(file_path, start_page, end_page):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(start_page-1, end_page): # индексация страниц начинается с 0
            text += reader.pages[page].extract_text()
    return text

text_from_inst= convert_pdf_to_text_range("inst.pdf", 2, 3)
text_from_oper= convert_pdf_to_text_range("inst.pdf", 2, 2)
# Удаление последовательности точек
cleaned_text_inst = re.sub(r'\.{2,}', '', text_from_inst)
cleaned_text_oper = re.sub(r'\.{2,}', '', text_from_oper)
# print(cleaned_text)
# Функция для фильтрации текста по заданному шаблону
def filter_by_pattern(text):
    return "\n".join([line for line in text.split("\n") if re.match(r'^\d+\.', line)])

filtered_text_i = filter_by_pattern(cleaned_text_inst)
filtered_text_o = filter_by_pattern(cleaned_text_oper)
print(filtered_text_i)
print(filtered_text_o)
# for page_num, text in enumerate(texts_from_pdf, 1): вывод всего текста с допоплнительной нумерацией страниц
#     print(f"------ Page {page_num} ------")
#     print(text)
#     print("-----------------------------\n")