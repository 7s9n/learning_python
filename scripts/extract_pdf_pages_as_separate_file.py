from PyPDF2 import (
    PdfFileReader,
    PdfFileWriter,
)

pdf_file_path = r"C:\Users\Hussein\Desktop\VT217_Asurveyonvoiceconversionusingdeeplearning.pdf"

file_base_name = pdf_file_path.replace('.pdf', '')

reader = PdfFileReader(pdf_file_path)

pages_to_extract = [11, 12]

writer = PdfFileWriter()

for page_num in pages_to_extract:
    writer.addPage(reader.getPage(page_num))

with open(f'{file_base_name}_subset.pdf', 'wb') as f:
    writer.write(f)