import PyPDF2
import os
#https://realpython.com/pdf-python/
def extract_information(pdf_path: str):
    if not os.path.exists(pdf_path):
        raise Exception(f"{pdf_path} doesn't exist")

    with open(pdf_path , 'rb') as pdf_file:

        pdf = PyPDF2.PdfFileReader(pdf_file)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        txt = f"""
        Information about {pdf_path}

        Author: {information.author}.
        Creator: {information.creator}.
        Producer: {information.producer}.
        Subject: {information.subject}.
        Title: {information.title}.
        Number of pages: {number_of_pages}.
        """

        print(txt)

    return information

def rotate_page(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_number in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_number).rotateClockwise(90)
        pdf_writer.addPage( page )

    output_path = os.path.join('.','output.pdf')
    with open(output_path , 'wb') as out_file:
        pdf_writer.write(out_file)

def merge_pdfs(paths , output_path):
    pdf_writer = PyPDF2.PdfFileWriter()

    for path in paths:
        if os.path.exists(path):
            pdf_reader = PyPDF2.PdfFileReader(path)
            # for page_number in range(pdf_reader.getNumPages()):
            #     page = pdf_reader.getPage(page_number)
            #     pdf_writer.addPage(page) # Add each page to the writer object
            pdf_writer.appendPagesFromReader(pdf_reader) # you can also use buil in function
    # Write out the merged PDF
    with open(output_path , 'wb') as out_file:
        pdf_writer.write(out_file)

def split_pdf(path , at):
    pass
if __name__ == '__main__':
    pdf_path = '../Desktop/python-crash-course.pdf'
    pdf_paths = []
    output_path = os.path.join('.' , 'output.pdf')

    extract_information(pdf_path)

    rotate_page(pdf_path)

    for root , dirs , files in os.walk('C:/Users/Hussein Sarea/Desktop/Course c++'):
        for file in files:
            pdf_paths.append(os.path.join(root , file))

    merge_pdfs(pdf_paths , output_path)
