def hello():
    print("Hello")
import tkinter
window=tkinter.Tk()
button=tkinter.Button(window,text='Hellooo',command=hello)
button.pack()
window.mainloop()