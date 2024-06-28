import tkinter
window=tkinter.Tk()
window.title("Spinbox tutorial")
#printing spinbox value
def spinPressed():
    print(spinvar.get())
#string variable to store spinbox value
spinvar=tkinter.StringVar()
spin=tkinter.Spinbox(window,from_=0,to=100,values=["hello","hi","yes","no"],textvariable=spinvar,command=spinPressed)
#values overwrites from and to
spin.pack()
window.mainloop()