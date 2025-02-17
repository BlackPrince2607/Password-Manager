from tkinter import *
from tkinter import messagebox
from random import shuffle,choice,randint
import pyperclip
import json
# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    webs = web_entry.get()
    with open("Pass.json",'r') as data_file:
        data = json.load(data_file)
        if webs in data:
            print(data)
            email = data[webs]["email"]
            p = data[webs]["password"]
            messagebox.showinfo(title=webs,message=f"Email:{email}\nPassword:{p}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10)) ]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4)) ]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4)) ]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webs = web_entry.get()
    p = password_entry.get()
    new_data = {
        webs:{
            "email":email_entry.get(),
            "password":p
        }
    }
    if len(webs) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="OOPS!",message="Make sure to not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(),message=f"These are the details entered \n"
                                    f"Email:{email_entry.get()}\nPassword: {password_entry.get()}\n Is it okay to save?")
        if is_ok:
            try:
                with open("Pass.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("Pass.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            else:
                data.update(new_data)        
                with open("Pass.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                web_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
photo = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1,columnspan=2,sticky='w')

website = Label(text="Website:")
website.grid(row=1,column=0)
web_entry = Entry(width=21)
web_entry.grid(row=1,column=1,columnspan=2,sticky='w')

email = Label(text="Email/Username:")
email.grid(row=2,column=0)
email_entry = Entry(width=39)
email_entry.insert(0,"soham@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky='w')

password = Label(text="Password:")
password.grid(row=3,column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,columnspan=1,sticky='w')

gen_butt = Button(text="Generate Password",command=gen_pass,width=14)
gen_butt.grid(row=3,column=2,sticky='w',padx=0)

search_butt = Button(text="Search",width=14,command=find_password)
search_butt.grid(row=1,column=2,sticky='w',padx=2)

add = Button(text="Add",width=33,command=save)
add.grid(row=4,column=1,columnspan=2,sticky='w')
window.mainloop()