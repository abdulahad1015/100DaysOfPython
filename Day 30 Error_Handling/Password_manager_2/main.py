from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate_password():
    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    for char in range(nr_numbers):
        password_list += random.choice(numbers)
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    Entry3.delete(0,END)
    Entry3.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=Entry1.get()
    email=Entry2.get()
    password=Entry3.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }

    if (len(website) == 0 or len(email) == 0 or len(password) == 0):
        messagebox.showinfo(title="Error ",message="Please Enter complete details.")
    else:
        try:
            with open("data.json", "r") as file:
                data=json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data,file,indent=4)

        Entry1.delete(0,END)
        Entry2.delete(0,END)
        Entry2.insert(0, "abdulahad1015@gmail.com")
        Entry3.delete(0,END)
        Entry1.focus()
        messagebox.showinfo(title="Title",message="Data Saved")

#-------------------------------Search----------------------------------#
def search():
    website=Entry1.get()
    email=""
    password=""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Website",message="No passwords saved")
    else:
        try:
            email=data[website]['email']
            password=data[website]['password']
        except KeyError:
            messagebox.showinfo(title="Website", message=f"No password for {website} saved")
        else:
            messagebox.showinfo(title="Website",message=f"Email: {email}\nPassword: {password}")
        Entry1.delete(0, END)
        Entry2.delete(0, END)
        Entry2.insert(0, "abdulahad1015@gmail.com")
        Entry3.delete(0, END)
        Entry1.focus()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager")
window.config(padx=50,pady=60)
window.iconbitmap("logo.ico")

lock_img=PhotoImage(file="logo.png")

canvas = Canvas(width=150,height=200)
canvas.create_image(89,100,image=lock_img)
canvas.grid(row=0,column=1)
#-------------------------Entries-----------------------------
Entry1=Entry(width=25)
Entry1.grid(row=1,column=1,columnspan=2,sticky="w")
Entry1.focus()

Entry2=Entry(width=45)
Entry2.grid(row=2,column=1,columnspan=2,sticky="w")
Entry2.insert(0,"abdulahad1015@gmail.com")

Entry3=Entry(width=25)
Entry3.grid(row=3,column=1,sticky="w")
#--------------------------Labels------------------------------
Label1=Label(text="Website:")
Label1.grid(row=1,column=0,sticky="w")

Label2=Label(text="Email/Username:")
Label2.grid(row=2,column=0,sticky="w")

Label3=Label(text="Password:")
Label3.grid(row=3,column=0,sticky="w")
#--------------------------Buttons------------------------------
Button1=Button(text="Generate Password",width=15,command=generate_password)
Button1.grid(row=3,column=2,sticky="w",padx=5,pady=5)

Button2=Button(text="Add",width=38,command=save)
Button2.grid(row=4,column=1,columnspan=2,sticky="w",pady=5)

Button3=Button(text="Search",width=15,command=search)
Button3.grid(row=1,column=2,columnspan=2,sticky="w",padx=5,pady=5)

window.mainloop()