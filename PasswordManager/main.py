from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_entry.delete(0, END)
    password_list = []

    password_list += [choice(letters) for _ in range(0, randint(8, 10))]
    password_list += [choice(symbols) for _ in range(0, randint(2, 4))]
    password_list += [choice(numbers) for _ in range(0, randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():  

    new_data = {website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if website_entry.get() and email_entry.get() and password_entry.get():
        try:
            with open(r"saved_passwords.json", mode="r") as data_file:
                data = json.load(data_file)
        
        except FileNotFoundError:      
            with open(r"saved_passwords.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4) 

        else:
            data.update(new_data)
            with open(r"saved_passwords.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4) 
            print(data)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        
        error = messagebox.showerror(message="Please fill all fields.", title="Incomplete Form", parent=window)
#-------------------------- SEARCH PASSWORD --------------------------- #
def search_password():
    request = website_entry.get() 
    try:
        with open("saved_passwords.json", mode="r") as data_file:
            data = json.load(data_file)
            dict_password = data[request]["password"]
            dict_email = data[request]["email"]
            
    except KeyError:
        key_error = messagebox.showerror(title="Error", message="No connected password to that site.")
    
    except FileNotFoundError:
        file_error = messagebox.showerror(title="Error", message="No passwords created yet.")
    
    else:
        password_info = messagebox.showinfo(title=request, message=f"Email: {dict_email}\nPassword: {dict_password}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
FONT = ("Ariel", 12, "normal")

def create_widget(widget_type, grid_x, grid_y, column_span=None, width=None, padx=0, pady=0, text=None, font=None, command=None, sticky=None):
    if widget_type.lower() == "label":
        new_label = Label(padx=padx, pady=pady, text=text, font=font)
        new_label.grid(sticky=sticky, column=grid_x, row=grid_y, columnspan=column_span)
        return new_label
    elif widget_type.lower() == "button":
        new_button = Button(padx=padx, pady=pady, text=text, width=width, font=font, command=command)
        new_button.grid(sticky=sticky, column=grid_x, row=grid_y, columnspan=column_span)
        return new_button
    elif widget_type.lower() == "entry":
        new_entry = Entry(text=text, font=font, width=width)
        new_entry.grid(sticky=sticky, column=grid_x, row=grid_y,  columnspan=column_span, padx=padx, pady=pady)
        return new_entry

#canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = create_widget(widget_type="Label", grid_x=0, grid_y=1, text="Website:", font=FONT)
website_entry = create_widget(widget_type="Entry", sticky="w", grid_x=1, grid_y=1, width=33, column_span=2)
search_button = create_widget(widget_type="Button", grid_x=2, grid_y=1, text="Search", width=14, command=search_password)
website_entry.focus()

email_label = create_widget(widget_type="Label", grid_x=0, grid_y=2, text="Email/Username:", font=FONT)
email_entry = create_widget(widget_type="Entry", sticky="w", grid_x=1, grid_y=2, width=52, column_span=2)
email_entry.insert(0, "kbiondich7@gmail.com")

password_label = create_widget(widget_type="Label", grid_x=0, grid_y=3, text="Password:", font=FONT)
password_entry = create_widget(widget_type="Entry", sticky="w", grid_x=1, grid_y=3, width=33)
password_gen_button = create_widget(widget_type="Button", sticky="w", grid_x=2, grid_y=3, text="Generate Password", command=generate_password)
password_add_button = create_widget(widget_type="Button", sticky="w", grid_x=1, grid_y=4, column_span=2, width=44, text="Add", command=save_password)

window.mainloop()