from tkinter import *

WINDOW_WIDTH = 250
WINDOW_HEIGHT = 150
FONT = ("Helvetica", 12, "normal")

window = Tk()
window.title("My first GUI program")
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
# Set the window in the middle of the screen
window_x = (window.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2)
window_y = (window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2)
# PULLED THIS FROM STACK OVERFLOW.  NEED TO RESEARCH EXACTLY WHAT IT IS DOING
# RESEARCHED: THE FOLLOWING IS JUST THE OLDER PYTHON 2 METHOD OF STRING FORMATTING
#             PYTHON 3 USES THE FSTRING AND CURLY BRACES
window.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, window_x, window_y))
# I DO NOT KNOW WHY THE FOLLOWING WON'T ALSO WORK.  NEED TO RESEARCH THE .geometry() METHOD IN TKINTER
# window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")

# ADD PADDING AROUND ALL WIDGETS
window.config(padx=5, pady=5)


# Function that we have mapped to the button click using the "command=" keyword argument
def miles_to_km():
    miles_input = float(user_input.get())
    km = round(miles_input * 1.609344, 2)
    display = "{:,.2f}".format(km)
    converted_kms.config(text=display, font=("Helvetica", 12, "bold"))


pad_x = 20
pad_y = 20


# Entry component, i.e. input
user_input = Entry(width=15)
user_input.grid(column=1, row=0)
# .get() is used to get user input from the Entry text input field.  It returns a string
# If input.get() were called here, then get() would not return anything as nothing as been entered at this time.
# .get() needs to be called after an event and then it can be triggered it
# HOW TO CREATE A LABEL
miles_label = Label(text="Miles", font=FONT, padx=pad_x, pady=pad_y)
# my_label["text"] = "New Text"
# OR
# HAVE TO USE A LAYOUT MANAGER TO GET CREATED WIDGETS ONTO THE SCREEN (PACK, PLACE, GRID)
# my_label.pack()
# my_label.place(x=100, y=200)
miles_label.grid(column=2, row=0, sticky="W"+"E")
equal_to = Label(text="is equal to", font=FONT)
equal_to.grid(column=0, row=1)
converted_kms = Label(text="", font=FONT)
converted_kms.grid(column=1, row=1)
km_label = Label(text="km", font=FONT)
km_label.grid(column=2, row=1, sticky="W"+"E")


# HOW TO CREATE BUTTONS
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)





# tkinter holds onto window in the while loop and listens for inputs
# This will keep window viewable and listening
window.mainloop()
