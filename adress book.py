from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
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
            deletee()
    else:
        messagebox.showerror("ERROR",'Please add a name')
def deletedic():
    mouse=listbox.curselection()
    if mouse:
        mous=listbox.get(mouse)
        del dictionary[mous]
        listbox.delete(mouse)
    else:
        messagebox.showerror('error','Nothing is selected')
def saveas():
    saved=asksaveasfile(defaultextension='.txt')
    if saved:
        print(dictionary,file=saved)
        listbox.delete(0,END)
        dictionary.clear()
    else:
        messagebox.showerror('ERROR','Please write in the file before trying to save')
def openfile():
    fileopen=askopenfile(title='openfile')
    if fileopen:
        global dictionary
        dictionary=eval(fileopen.read())
        for i in dictionary.keys():
            listbox.insert(END,i)
    else:
        messagebox.showerror('ERROR','Select A Valid File')

def editfile():
    







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
save=Button(frame,text='SAVE',command=saveas)
save.pack(pady=60)
open=Button(root,text='OPEN',command=openfile)
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
delete=Button(root,text='DELETE',command=deletedic)
delete.place(y=400,x=150)



root.mainloop()