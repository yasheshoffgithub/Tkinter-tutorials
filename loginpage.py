import tkinter
from tkinter import messagebox
window= tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')
#login functionality
def login():
    username="johnsmith"
    password="12345"
    if username_entry.get()==username and passWord_entry.get()==password:
        messagebox.showinfo(title="Login message",message="Login Successful")
    else:
        messagebox.showinfo(title="Error message",message="Invalid Login.Plesae try again")
#adding responsiveness
frame=tkinter.Frame(bg='#333333')
#creating widgets
login_label=tkinter.Label(frame,text="Login",bg='#333333',fg="#FF3399",font=("Arial",30))
username_label=tkinter.Label(frame,text="Username",bg='#333333',fg="#FFFFFF",font=("Arial",16))
username_entry=tkinter.Entry(frame,font=("Arial",16))
passWord_entry=tkinter.Entry(frame,show="*",font=("Arial",16))
passWord_label=tkinter.Label(frame,text="Password",bg='#333333',fg="#FFFFFF",font=("Arial",16))
login_button=tkinter.Button(frame,text="LOGIN",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command=login)
#placing widgets on the screen
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
passWord_label.grid(row=2,column=0)
passWord_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)
#place the frame
frame.pack()
window.mainloop()
