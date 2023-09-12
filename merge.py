from PyPDF2 import PdfMerger
import os

cwd = os.getcwd()
cwd = os.path.join(cwd, "pdf_files")
filelist = os.listdir(cwd)
print(filelist)

merger = PdfMerger()

for file in filelist:
    merger.append(os.path.join(cwd, file))

merger.write("Merged.pdf")
merger.close
