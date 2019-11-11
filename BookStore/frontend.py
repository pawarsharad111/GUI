from tkinter import *
from backend import *

def view_command():
    list1.delete(0,END)
    result=view()
    for i in result:
        list1.insert(END,i)

def search_command():
    list1.delete(0, END)
    result =search(title_text.get(),author_text.get(),isbn_text.get(),year_text.get())
    for i in result:
        list1.insert(END, i)

def insert_command():
    insert(title_text.get(),author_text.get(),isbn_text.get(),year_text.get())
    list1.delete(0, END)
    list1.insert(END,title_text.get(),author_text.get(),isbn_text.get(),year_text.get())

def delete_command():
    delete(title_text.get())


window=Tk()
window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(window,text="author")
l2.grid(row=0,column=2)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=4)

l3=Label(window,text="year")
l3.grid(row=1,column=0)


year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

l4=Label(window,text="isbn")
l4.grid(row=1,column=2)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=4)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6, columnspan=2)

sbl=Scrollbar(window)
sbl.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sbl)
sbl.configure(command=list1.yview())

b1=Button(window,text='View all',command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="search entry",command=search_command)
b2.grid(row=3,column=3)

b4=Button(window,text="insert",command=insert_command)
b4.grid(row=5,column=3)

b5=Button(window,text="delete",command=delete_command)
b5.grid(row=6,column=3)


window.mainloop()