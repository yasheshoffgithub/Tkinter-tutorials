def hello():
    print("Hello world")

import tkinter
if __name__ == '__main__':
    window=tkinter.Tk()
    def printHello():
        print(textentry.get())    
    window.title("Yashesh First Tkinter App")
    window.geometry('600x400')
    label=tkinter.Label(window,text="Hello World",bg="red",fg="blue")
    label.pack()
    textentry=tkinter.Entry(window)
    textentry.pack()
    button=tkinter.Button(window,text="Hello World",bg="black",fg="white",command=printHello)
    button.pack()
    window.mainloop()
