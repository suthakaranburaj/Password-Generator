from tkinter import *
from tkinter import messagebox
import json
import csv


def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data File found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    return password

def generate():
    pass_generated = password_generator()
    Password_input.insert(0,pass_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    user_gmail=Email_input.get()
    user_password=Password_input.get()
    new_data ={website:{
        "email":user_gmail,
        "password":user_password
    }}

    if len(user_gmail)==0 or len(website) ==0 or len(user_password)==0:
        messagebox.showerror(title="Oops",message="Please make sure you haven't left any fields empty")

    else:
        try:
            with open("data.json","r") as data_file:
                #reading old data
                data =json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                #saving update
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            Password_input.delete(0, END)
            Email_input.delete(0, END)
            Email_input.insert(0, user_gmail)






# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.minsize(width=600,height=600)

canvas = Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()


Email_label=Label(text="Email/Username:")
Email_label.grid(row=2,column=0)
Email_input=Entry(width=40)
Email_input.grid(row=2,column=1,columnspan=2)


Password_label=Label(text="Password:")
Password_label.grid(row=3,column=0)
Password_input=Entry(width=21)
Password_input.grid(row=3,column=1)


Generate_button=Button(text="Generate Password",command=generate)
Generate_button.grid(row=3,column=2)

Add_button=Button(text="Add",width=35,command=save)
Add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search" ,width=15,command=find_password)
search_button.grid(row=1,column=2)






window.mainloop()