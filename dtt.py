import docx
import os

DIR_PATH = "docx"
DIR_PATH_TXT = "txt"

def get_filenames():
    file_names = [
        f for f in os.listdir(DIR_PATH) if os.path.isfile(os.path.join(DIR_PATH, f))
    ]
    return file_names

def create_txt(doc, file_name):
    txt = file_name.replace(".docx", ".txt")
    f = open(f"{DIR_PATH_TXT}/{txt}", "w", encoding='utf-8')
    for paragraph in doc.paragraphs:
        f.write(paragraph.text + "\n")
    f.close()
    print(f"Created: {txt}")

def open_docx(dir):
    document = docx.Document(dir)
    # create_txt(document)
    return document

def docx_to_txt():
    fs = get_filenames()
    for f in fs:
        doc = open_docx(f"{DIR_PATH}/{f}")
        create_txt(doc, f)

docx_to_txt()