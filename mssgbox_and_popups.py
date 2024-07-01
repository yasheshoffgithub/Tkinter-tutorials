import tkinter
from tkinter import messagebox #you have to explicitly import it 

def openMessageBox():
    # messagebox.showinfo(title="Info message", message="This is an info message")
    # messagebox.showerror(title="Error",message="You made an error")
    # messagebox.showwarning(title="Warning",message="Do not close this")
    #res_ques=messagebox.askquestion(title="Question",message="Do you wish to proceed?")#stores yes/no
    #print(res_ques)
    #res_yesno=messagebox.askyesno(title="Question",message="Do you wish to proceed?") #stores true/false
    #print(res_yesno)
    #res=messagebox.askretrycancel(title="Question",message="Do you wish to retry?")
    # res=messagebox.askokcancel(title="Question",message="Do you wish to proceed") #true/false
    # print(res)
    res=messagebox.askyesnocancel(title="Question",message="Do you wish to proceed?") 
    print(res)
    if res is None:
        print("User cancelled") 
window=tkinter.Tk()
button=tkinter.Button(window,text="Press Me",command=openMessageBox)
button.pack()
window.mainloop()