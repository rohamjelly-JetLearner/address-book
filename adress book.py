from tkinter import *
from tkinter import messagebox
root=Tk()
dictionary={}
def deletee():
    name1.delete(0,END)
    adress1.delete(0,END)
    mobile1.delete(0,END)
    email1.delete(0,END)
    birthday1.delete(0,END)
def update():
    nm=name1.get()
    if nm != '' :
        if nm not in dictionary.keys():
            listbox.insert(END,nm)
            dictionary[nm]=[adress1.get(),mobile1.get(),email1.get(),birthday1.get()]
            print(dictionary)
            deletee()
    else:
        messagebox.showerror("ERROR",'Please add a name')
def deltedic():
    mouse=listbox.curselection()
    mouse=listbox.get(mouse)
    




root.geometry('500x500')
frame=Frame(root)
frame.place(x=225,y=0)
name=Label(frame,text='NAME:')
name.pack(pady=30)
adress=Label(frame,text='ADDRESS:')
adress.pack(pady=30)
mobile=Label(frame,text='MOBILE:')
mobile.pack(pady=30)
email=Label(frame,text='EMAIL:')
email.pack(pady=30)
birthday=Label(frame,text='BIRTHDAY:')
birthday.pack(pady=30)
save=Button(frame,text='SAVE')
save.pack(pady=60)
open=Button(root,text='OPEN')
open.place(x=175,y=0)
frame1=Frame(root)
frame1.place(x=325,y=0)
name1=Entry(frame1)
name1.pack(pady=30)
adress1=Entry(frame1)
adress1.pack(pady=30)
mobile1=Entry(frame1)
mobile1.pack(pady=30)
email1=Entry(frame1)
email1.pack(pady=30)
birthday1=Entry(frame1)
birthday1.pack(pady=30)
upd=Button(frame1,text='UPDATE/ADD',command=update)
upd.pack(pady=30)
listbox=Listbox(root,bg='red',width=25,height=22)
scrollbar=Scrollbar(listbox,orient='vertical')
listbox.place(x=0,y=0)
#scrollbar.place(x=135,y=0)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
edit=Button(root,text='EDIT')
edit.place(y=400,x=50)
delete=Button(root,text='DELETE')
delete.place(y=400,x=150)
root.mainloop()