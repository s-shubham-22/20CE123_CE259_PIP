from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
pdf = PdfFileReader(str("University Result.pdf"))
pdf_writer = PdfFileWriter()

print(pdf.getNumPages())
for page in pdf.pages:
    print(page.extractText())
    pdf_writer.addPage(page)

with Path("Result.pdf").open("wb") as output:
    pdf_writer.write(output)

# Github Repo Link: https://github.com/s-shubham-22/20CE123_CE259_PIP