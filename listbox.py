import tkinter

window=tkinter.Tk()
window.title("listbox tutorial")
def listSelected(event):
    print(listbox.get(listbox.curselection()))
listvar=tkinter.StringVar(value=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
listbox=tkinter.Listbox(window,listvariable=listvar,height=7,selectmode='extended')
listbox.pack()
listbox.bind('<<ListboxSelect>>',listSelected)
window.mainloop()