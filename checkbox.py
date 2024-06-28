import tkinter
window=tkinter.Tk()
window.title("Checkbox tutorial")
window.geometry('340x440')
#function to record value of checkbox
def checkPressed():
    print(checkvar.get())
#save checkbox value
checkvar=tkinter.StringVar()
check=tkinter.Checkbutton(window,text="Click Me!",variable=checkvar,onvalue="yes",offvalue="no",command=checkPressed)
check.pack()
window.mainloop()