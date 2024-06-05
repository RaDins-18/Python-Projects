# QUESTION:
# Write a python program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.



# SOLUTION:

# Importing important modules.
from PyPDF2 import PdfWriter
import os

# Set merger with PdfWriter(), It is like a new blank pdf file.
merger = PdfWriter()

# Gets all pdf files from (PDF Files) folder in a list.
files = [file for file in os.listdir("PDF Files") if file.endswith(".pdf")]

# For loop for getting each file.
for pdf in files:
    # Add pdf file to the end of a blank pdf file.
    merger.append(f"PDF Files/{pdf}")

# Set the name of merger (new pdf file) in the (Merged PDF File) folder.
merger.write("Merged PDF File/result.pdf")

# Close the merger (complete new pdf file).
merger.close()