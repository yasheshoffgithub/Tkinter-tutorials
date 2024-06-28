import tkinter
window=tkinter.Tk()
def gettext():
    print(text.get("1.0","end")) #start from line 1 char0 to the end of text
#creating text
text=tkinter.Text(window,width=80,height=15,font=("Arial",20))

text.pack()

get_bttn=tkinter.Button(window,text="Get Text",command=gettext)
get_bttn.pack()
def inserttext():
    text.insert('1.0','just inserted at start')
insert_bttn=tkinter.Button(window,text="Insert Text",command=inserttext)
insert_bttn.pack()
def deletetext():
    text.delete('2.0','end')
delete_bttn=tkinter.Button(window,text="Delete Text",command=deletetext)
delete_bttn.pack()
window.mainloop()