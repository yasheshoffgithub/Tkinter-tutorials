import tkinter
from tkinter import ttk #kindof a submodule for themes

window=tkinter.Tk()
window.title("Combobox tutorial")
window.geometry('340x440')
def comboFunction(event):
    print(combo.get())
combo=ttk.Combobox(window,values=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
combo.pack()
combo.set("Select day") #default value
#record info in combobox- binding the selected value to a function
combo.bind('<<ComboboxSelected>>',comboFunction)
combo["state"]='readonly' #to not allow user to write
window.mainloop()