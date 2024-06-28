import tkinter
def totalprice():
    totalprice=int(priceperitem_entry.get())*int(numberofitems_entry.get())
    totalprice_entry.insert(0,string=str(totalprice))
window= tkinter.Tk()
window.title("Responsive Grid")
#using frame to make it repsonsive
frame=tkinter.Frame(window)

#widgets
priceperitem_label=tkinter.Label(frame,text="Price per item")
priceperitem_entry=tkinter.Entry(frame)
numberofitems_label=tkinter.Label(frame,text="Number of items")
numberofitems_entry=tkinter.Entry(frame)
totalprice_label=tkinter.Label(frame,text="Total price")
totalprice_entry=tkinter.Entry(frame)
totalprice_button=tkinter.Button(frame,text="Calculate total price",command=totalprice)
#using grid to align widgets
priceperitem_label.grid(row=0,column=0)
priceperitem_entry.grid(row=0,column=1)
numberofitems_label.grid(row=1,column=0)
numberofitems_entry.grid(row=1,column=1)
totalprice_label.grid(row=2,column=0)
totalprice_entry.grid(row=2,column=1)
totalprice_button.grid(row=3,column=0,columnspan=2)
frame.pack()
window.mainloop()