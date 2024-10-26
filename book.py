from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("700x550")
window.config(bg="#3456ad")
window.title("CONTACT BOOK")

contact=[
    ["Alexander","2704190895"],
    ["Jalil","4054924867"],
    ["aex","5963952021"],
    ["epsj","3756839449"],
    ["erllfkgni","9472495338"],
    ["sapewvwegewvw","3757464235"],
    ["fvrbhuernnriv","1234567890"],
    ["Thomas","0987654321"],
    ["Vinny","2143658709"],
    ["Sam","1324576890"],
    ["Ken","0897645321"],
    ["Ibraheem","1029384756"],
    ["dvgesvsgsrge","3948576240"],
    
    ]
Name = StringVar()
Number = StringVar()

frame=Frame(window)
frame.pack(side=RIGHT)
scroll=Scrollbar(frame,orient=VERTICAL)
select=Listbox(frame,yscrollcommand=scroll.set, font =("Times new roman",16),bg="#ffffff",width=20,height=20,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side = LEFT,fill=BOTH,expand=1)

def Selected():
    print("Hello",len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error","please select the name")
    else:
        return int(select.curselection()[0])
    
def addContact():
    if Name.get()=="" and Number.get()!="":
        contact.append([Name.get(),Number.get()])
        print(contact)
        Select_set()
        entryReset()
        messagebox.showinfo("confirmation","Successfully added contact")
    else:
        messagebox.showerror("Error","Failed to add contact")

def updateDetails():
    if Name.get() and Number.get():
        contact[Selected()]=[Name.get(),Number.get()]
        messagebox.showinfo("confirmation","Successfully updated contact")
        entryReset()
        Select_set()
    elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
         messagebox.showerror("Error","Please fill the information")
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error","Please select the name")
        else:
            message1 = """none"""
            messagebox.showerror("Error",message1)

def entryReset():
    Name.set('')
    Number.set('')

def delete_entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno("Confirmation","Do you want to delete contact\n Which you have selected")
        if result == TRUE:
            del contact[Selected()]
            Select_set()
        else:
            messagebox.showerror("error","please select the contact")

def view():
    NAME,PHONE=contact[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
def exit():
    window.destroy()

def Select_set():
    contact.sort()
    select.delete(0,END)
    for name,phone in contact:
        #select.insert(END,phone)
        select.insert(END,name)
Select_set()
    

Label(window,text="Name",font=("Times New Roman",21,"bold"),bg="yellow").place(x=30,y=20)
Entry(window,width=30).place(x=200,y=30)
Label(window,text="Contact NO.",font=("Times New Roman",21,"bold"),bg="yellow").place(x=30,y=70)
Entry(window,width=30).place(x=200,y=80)

Button(window,text="ADD",font="Helvetica 18 bold",bg="pink",padx=20, command=addContact).place(x=50,y=140)
Button(window,text="EDIT",font="Helvetica 18 bold",bg="pink",padx=20,command=updateDetails).place(x=50,y=200)
Button(window,text="VIEW",font="Helvetica 18 bold",bg="pink",padx=20,command=view).place(x=50,y=260)
Button(window,text="RESET",font="Helvetica 18 bold",bg="pink",padx=20,command=entryReset).place(x=50,y=320)
Button(window,text="DELETE",font="Helvetica 18 bold",bg="pink",padx=20,command=delete_entry).place(x=50,y=380)
Button(window,text="EXIT",font="Helvetica 18 bold",bg="red",padx=20,command=exit).place(x=300,y=440)


window.mainloop()