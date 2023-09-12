from tkinter import filedialog
from PyPDF2 import PdfMerger

filelist = filedialog.askopenfilenames(filetypes=[('PDF files', '*.pdf')], title="Dateien zum zusammenfügen auswählen")
print(filelist)

merger = PdfMerger()

for file in filelist:
    merger.append(file)

save = filedialog.asksaveasfilename(filetypes=[('PDF files', '*.pdf')], title="Datei speichern unter")
merger.write(save)
merger.close
