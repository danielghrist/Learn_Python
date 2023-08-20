from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
learning_lang = "Spanish"
current_card = {}

# Pull data from file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/spanish_words.csv")
finally:
    words_to_learn = data.to_dict(orient="records")


# Create Flash card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfigure(card_background, image=card_front)
    canvas.itemconfigure(card_title, text=learning_lang, fill="black")
    canvas.itemconfigure(card_word, text=current_card[learning_lang], fill="black")
    flip_timer = window.after(3000, func=flip_card)


# Flip Card Image front to back
def flip_card():
    # Show back of the card with English word
    canvas.itemconfigure(card_background, image=card_back)
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_word, text=current_card["English"], fill="white")


# Remove learned word
def remove_learned():
    try:
        words_to_learn.remove(current_card)
        df = pandas.DataFrame(words_to_learn)
        df.to_csv("./data/words_to_learn.csv", index=False)
    except ValueError:
        print("You learned all the words!  Congratulations!")
    except IndexError:
        print("For god's sake he's already dead!")
    else:
        pass
    finally:
        next_card()


# Create GUI
# Create Window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Create Canvas for front of card and back of card to switch between
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Helvetica", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Helvetica", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="news")

# Create Buttons
x_image = PhotoImage(file="./images/wrong.png")
reject = Button(image=x_image, fg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
reject.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
accept = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=remove_learned)
accept.grid(row=1, column=1)

next_card()

window.mainloop()
