import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from pathlib import Path

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 400
LABEL_Y_PADDING = 5
DARK_BLUE = "#2A0944"
FONT = ("Helvetica", 11, "normal")
# Create a relative file path to the current folder the main.py file is in using pathlib module:
REL_FILE_PATH = Path(__file__, "../").resolve()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generates password of 3 symbols, 5 letters, and 3 numbers
def generate_password():
    password_entry.delete(0, END)
    num_letters = 8
    num_numbers = 3
    num_symbols = 4
    password_dict = {
        "letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "symbols": ["!", "*", "?", ",", "-", "/", "@", "#", "$", "%", "^", "^", "&", "*", "(", ")", "+"]
    }

    password_letters = [random.choice(
        password_dict["letters"]) for _ in range(num_letters)]
    password_numbers = [random.choice(
        password_dict["numbers"]) for _ in range(num_numbers)]
    password_symbols = [random.choice(
        password_dict["symbols"]) for _ in range(num_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open(REL_FILE_PATH.joinpath("password_db.json"), "r") as password_db:
            saved_passwords = json.load(password_db)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="You do not have any saved passwords.")

    else:
        if website in saved_passwords:
            messagebox.showinfo(title=f"{website}", message=f"Email/Username: {saved_passwords[website]['user_name']}\n"
                                f"Password: {saved_passwords[website]['password']}")

        else:
            messagebox.showinfo(
                title="Not Found", message="You do not have a password stored for this website.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Adds the entered information from the user into the saved txt file


def add_password():
    website = website_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()
    new_password = {
        website: {
            "user_name": user_name,
            "password": password
        }
    }

    # Check to see if all information form boxes are filled out
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing Field",
                            message="Please fill out all fields.")
    else:
        try:
            password_db = open("password_db.json", "r")

        except FileNotFoundError:
            with open(REL_FILE_PATH.joinpath("password_db.json"), "w") as password_db:
                json.dump(new_password, password_db, indent=4)

        else:
            # Reading old data
            data = json.load(password_db)
            # Update old data
            data.update(new_password)
            # Update Data JSON File
            with open(REL_FILE_PATH.joinpath("password_db.json"), "w") as password_db:
                json.dump(data, password_db, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus_set()


# ---------------------------- IS WEBSITE ALREADY IN SAVE DATA ------------------------------- #
#
# def website_in_savedata(website, save_data):
#     if website in save_data:
#         return True
#     else:
#         return False
#

# ---------------------------- UI SETUP ------------------------------- #
# Create main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=DARK_BLUE)
screen_width = window.winfo_width()
screen_height = window.winfo_height()
# window_x = (screen_width / 2) - (WINDOW_WIDTH / 2)
# window_y = (screen_height / 2) - (WINDOW_HEIGHT / 2)
# window.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, window_x, window_y))
window.minsize(width=600, height=550)

main_frame = Frame(window, width=screen_width - 50,
                   height=screen_height - 50, bg=DARK_BLUE, padx=50, pady=50)
main_frame.pack()


# Create canvas
canvas = Canvas(master=main_frame, width=120, height=200,
                bg=DARK_BLUE, highlightthickness=0)
logo_img = PhotoImage(file=REL_FILE_PATH.joinpath("logo.png"))
canvas.create_image(60, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=LABEL_Y_PADDING)

# Create Labels
website_label = Label(master=main_frame, text="Website: ",
                      bg=DARK_BLUE, fg="white", pady=LABEL_Y_PADDING, font=FONT)
website_label.grid(row=1, column=0, sticky="w")

email_label = Label(master=main_frame, text="Email/Username: ",
                    bg=DARK_BLUE, fg="white", pady=LABEL_Y_PADDING, font=FONT)
email_label.grid(row=2, column=0, sticky="w")

password_label = Label(master=main_frame, text="Password: ",
                       bg=DARK_BLUE, fg="white", pady=LABEL_Y_PADDING, font=FONT)
password_label.grid(row=3, column=0, sticky="w")

# Create Entry boxes
website_entry = Entry(master=main_frame, width=20, font=FONT)
website_entry.focus_set()
website_entry.grid(row=1, column=1, columnspan=1, sticky="w")

email_entry = Entry(master=main_frame, width=40, font=FONT)
email_entry.insert(0, "danielghrist@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="we")

password_entry = Entry(master=main_frame, width=20, font=FONT)
password_entry.grid(row=3, column=1, sticky="w")

# Create Buttons
search_button = Button(master=main_frame, text="Search",
                       font=FONT, command=search)
search_button.grid(row=1, column=2, sticky="ew")

generate_button = Button(
    master=main_frame, text="Generate Password", font=FONT, command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(master=main_frame, text="Add",
                    width=34, font=FONT, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
