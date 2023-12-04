import os
import pandas as pd
from docx import Document
from reportlab.pdfgen import canvas

# Excelファイルのパス
xls_path = '/Users/kamehaku/Desktop/Add-LLM vs Chat-GPT/tools/DataX/aj10.xls'
# DataSetフォルダのパス
dataset_path = '/Users/kamehaku/Desktop/Add-LLM vs Chat-GPT/tools/DataSet/'

# Excelファイルを読み込む（数値データを文字列として解析）
df = pd.read_excel(xls_path, dtype=str)

# DataFrameをtxtファイルとして保存
txt_filename = os.path.join(dataset_path, 'aj10.txt')
with open(txt_filename, 'w', encoding='utf-8') as text_file:
    text_file.write(df.to_string(index=False))

# DataFrameをdocxファイルとして保存
docx_filename = os.path.join(dataset_path, 'aj10.docx')
doc = Document()
for index, row in df.iterrows():
    doc.add_paragraph(str(row.values))
doc.save(docx_filename)

# DataFrameをPDFファイルとして保存
pdf_filename = os.path.join(dataset_path, 'aj10.pdf')
c = canvas.Canvas(pdf_filename)
for index, row in enumerate(df.values.tolist()):
    c.drawString(72, 800 - 12 * index, str(row))
c.save()
