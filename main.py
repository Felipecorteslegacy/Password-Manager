from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Times New Roman", 12, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    p1 = [random.choice(letters) for num in range(nr_letters)]
    p2 = [random.choice(symbols) for num in range(nr_symbols)]
    p3 = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = p1 + p2 + p3

    random.shuffle(password_list)

    passwordd = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, passwordd)

    pyperclip.copy(passwordd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_ = web_entry.get()
    user_ = user_entry.get()
    password_ = password_entry.get()
    new_data = {
        website_: {
            "email": user_,
            "password": password_,
        }
    }

    if len(website_) == 0 or len(password_) == 0:
        messagebox.showinfo(title="Daaamn", message="You left some fields empty. Check it out!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data in order to update it
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Searching ------------------------------- #
def search_data():
    with open("data.json", mode="r") as file:
        data = json.load(file)
    item_to_be_search = web_entry.get()
    try:
        data[item_to_be_search]
    except KeyError:
        messagebox.showinfo(title="Data not found", message=f"{item_to_be_search} is not in your saved data.")
    else:
        user__ = data[item_to_be_search]["email"]
        password__ = data[item_to_be_search]["password"]
        messagebox.showinfo(title=item_to_be_search, message=f"Username: {user__}\nPassword: {password__}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("The ultimate password Manager")
window.config(padx=30, pady=30)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website = Label(text="Website:", font=FONT)
website.grid(row=1, column=0)

user = Label(text="Email/username:", font=FONT)
user.grid(row=2, column=0)

password = Label(text="Password:", font=FONT)
password.grid(row=3, column=0)

# Entries

web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()  # This will put the mouse in this entry

user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "felipecortesbusiness@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons

generate_button = Button(text="Generate Password", command=generate_pw)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()
