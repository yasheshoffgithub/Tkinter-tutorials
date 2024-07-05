import tkinter, PyPDF2
from tkinter import filedialog


root=tkinter.Tk()
root.title("PDF Text Extractor")

def openfile():
    filename = filedialog.askopenfilename(
        title="Open PDF file",
        initialdir=r'C:\Users\sarik\Desktop',
        filetypes=[('PDF files', '*.pdf')]
    )
    print(filename)
    filename_label.configure(text=filename)
    outputfile_text.delete("1.0",tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        outputfile_text.insert(tkinter.END,current_text)
filename_label=tkinter.Label(root,text="No File Selected")
outputfile_text=tkinter.Text(root)
outputfile_button=tkinter.Button(root,text="Open PDF File",command=openfile)

filename_label.pack()
outputfile_text.pack()
outputfile_button.pack()
root.mainloop()