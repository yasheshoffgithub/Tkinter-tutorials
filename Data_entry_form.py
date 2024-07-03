import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
#functions
def enter_data():
    accepted=accept_var.get()
    if accepted=="Accepted":
    #user info
        fname=first_name_entry.get()
        lname=last_name_entry.get()
        if fname and lname:
            title=title_combobox.get()
            age=age_spinbox.get()
            nationality=nationality_combobox.get()

            #course info
            registered_status=reg_status_var.get()
            numcourses=numcourses_spinbox.get()
            numsemesters=numsemesters_spinbox.get()
            print("First name:",fname, "Last name:",lname)
            print("Title:",title, "Age:",age)
            print("#Courses: ",numcourses,"# Semesters: ",numsemesters)
            print("Registeration Status: ",reg_status_var)
        else:
            tkinter.messagebox.showwarning(title="Error",message="Enter First Name and Last Name")   
    else: 
        tkinter.messagebox.showwarning(message="accept terms and conditions",title="Warning")   
window=tkinter.Tk()
window.title("Data Entry Form")
frame=tkinter.Frame(window)
frame.pack()
#saving user info
user_info_frame=tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=10)
first_name_Label=tkinter.Label(user_info_frame,text="First Name")
first_name_Label.grid(row=0,column=0)
last_name_Label=tkinter.Label(user_info_frame,text="Last Name")
last_name_Label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label=tkinter.Label(user_info_frame,text="Title")
title_combobox=ttk.Combobox(user_info_frame,values=["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame,from_=18,to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox=ttk.Combobox(user_info_frame,values=["INDIA","AUSTRALIA","PAKISTAN","ENGLAND","NEW ZEALAND","SOUTH AFRICA","AFGHANISTAN"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#saving course info
course_frame=tkinter.LabelFrame(frame)
course_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

reg_status_var=tkinter.StringVar(value="Not Registered")
registered_label=tkinter.Label(course_frame,text="Registeration Status")
registered_check=tkinter.Checkbutton(course_frame,text="Currently Registered",variable=reg_status_var,onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label=tkinter.Label(course_frame,text="# Completed Courses")
numcourses_spinbox=tkinter.Spinbox(course_frame,from_=0,to="infinity")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label=tkinter.Label(course_frame,text="# Semesters")
numsemesters_spinbox=tkinter.Spinbox(course_frame,from_=0,to="infinity")
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)
for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Accept terms
terms_frame=tkinter.LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,sticky="news", padx=20,pady=10)
accept_var=tkinter.StringVar(value="Not Accepted")
terms_check=tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions.",variable="Accepted",offvalue="Not Available")
terms_check.grid(row=0,column=0)


#buttons
button=tkinter.Button(frame,text="Enter Data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=20)
window.mainloop()