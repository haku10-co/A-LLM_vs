import os
import pdfplumber
from docx import Document

# PDFファイルのパス
pdf_path = '/Users/kamehaku/Desktop/Add-LLM vs Chat-GPT/tools/DataSet/ecoArxiv.pdf'
# DataSetフォルダのパス
dataset_path = '/Users/kamehaku/Desktop/Add-LLM vs Chat-GPT/tools/DataSet/'

# 出力ファイル名をPDFファイル名と同じにする
base_name = os.path.splitext(os.path.basename(pdf_path))[0]

# PDFファイルを開く
with pdfplumber.open(pdf_path) as pdf:
    # テキストを抽出
    text = '\n'.join(page.extract_text() for page in pdf.pages)

# txtファイルとして保存
txt_filename = os.path.join(dataset_path, f'{base_name}.txt')
with open(txt_filename, 'w', encoding='utf-8') as f:
    f.write(text)

# docxファイルとして保存
docx_filename = os.path.join(dataset_path, f'{base_name}.docx')
doc = Document()
doc.add_paragraph(text)
doc.save(docx_filename)