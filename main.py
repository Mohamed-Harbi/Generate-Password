import tkinter
from  tkinter import *
from tkinter import messagebox
import random
from tkinter.messagebox import showinfo
from typing import final

import pyperclip
import json



window = Tk()
window.title("password manager")
window.config(pady=20, padx=20)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def set_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_list_letter = [random.choice(letters) for x in range(nr_letters)]

    password_list_num = [random.choice(numbers) for x in range(nr_numbers)]

    password_list_sym = [random.choice(symbols) for x in range(nr_symbols)]


    password_list = password_list_letter + password_list_sym + password_list_num
    random.shuffle(password_list)

    password_x = "".join(password_list)
    input_pas.insert(0, password_x)
    #zpyperclip.copy(password_x)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def button_add():
    password= input_pas.get()
    email = input_email.get()
    web = input_web.get()
    new_data = {
        web:{
            "email": email,
            "password": password,

        }


    }

    if password == "" or email == "" or web == "":
        messagebox.showinfo(message="Details not compeleted")

    else:
       try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
       except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

       else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

       finally:
            input_web.delete(0, END)
            input_pas.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    website_label = input_web.get()
    try:
     with open("data.json") as data:
         website = json.load(data)
    except (FileNotFoundError, json.JSONDecodeError):
       messagebox.showinfo(message="NO Data File Found" )

    else:
        if website_label in website:
            email = website[website_label]["email"]
            password = website[website_label]["password"]
            messagebox,showinfo(title=website_label, message=f"Email: {email}\nPassword: {password} ")
        else:
            messagebox.showinfo(message="No data of the website", title="Error")







canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label= tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

input_web = tkinter.Entry(width=21)
input_web.grid(row=1, column=1)

input_email = tkinter.Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "mohamed harbi")

input_pas = tkinter.Entry(width=21)
input_pas.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generat Password", command=set_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=button_add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, columnspan=3)
























window.mainloop()




























