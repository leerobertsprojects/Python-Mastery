import PyPDF2
import sys

# inputs = sys.argv[1:]

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('crooked.pdf', 'wb') as New_file:
#         writer.write(New_file)

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf, 'merged')
#         merger.append(pdf)
#     merger.write('super.pdf')
#
# pdf_combiner(inputs)

# add watermark to pages

with open('super.pdf', 'rb') as file:
    pdf = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    with open('wtr.pdf', 'rb') as watermark_file:
        watermark = PyPDF2.PdfFileReader(watermark_file)
        for page in range(pdf.getNumPages()):
            pdfpage = pdf.getPage(page)
            pdfpage.mergePage(watermark.getPage(0))
            writer.addPage(pdfpage)
        with open('water_super.pdf', 'wb') as output_file:
            writer.write(output_file)














