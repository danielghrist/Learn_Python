from tkinter import *
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#008000"
YELLOW = "#f7f5dd"
DARK_SLATE_BLUE = "#483D8B"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 350
# Create a relative file path to the current folder the main.py file is in using pathlib module:
REL_FILE_PATH = Path(__file__, "../").resolve()

# ---------------------------- GLOBALS ------------------------------- #

reps = 0
timer = None
window = Tk()


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown_timer(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        window.deiconify()
        window.update()
    elif reps % 2 == 0:
        countdown_timer(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        window.deiconify()
        window.update()
    else:
        countdown_timer(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        window.deiconify()
        window.update()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown_timer(count):
    global timer
    minutes = int(count / 60)
    seconds = int(count % 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    window.title(f"Pomodoro Timer - {minutes:02}:{seconds:02}")
    if count > 0:
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps / 2)):
            marks += "✔"
        checks_label.config(text=marks)


# window.after(10, countdown_timer, time.gmtime().tm_min)

# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro Timer")
# window_x = (window.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2)
# window_y = (window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2)
# window.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, window_x, window_y))
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(bg=DARK_SLATE_BLUE, padx=100, pady=50)

# Create canvas.  Used for layering images/things
canvas = Canvas(width=200, height=224,
                bg=DARK_SLATE_BLUE, highlightthickness=0)
tomato_img = PhotoImage(file=REL_FILE_PATH.joinpath("tomato.png"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1, sticky="EW")

# Create Labels
timer_label = Label(text="Timer", bg=DARK_SLATE_BLUE,
                    fg=GREEN, anchor="n", font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0, sticky="new")
checks_label = Label(text="", bg=DARK_SLATE_BLUE, fg=GREEN,
                     anchor="center", font=(FONT_NAME, 15, "bold"))
checks_label.grid(column=1, row=3)

# Create Buttons
start_button = Button(text="Start", font=(
    FONT_NAME, 10, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2, sticky="e")

reset_button = Button(text="Reset", font=(
    FONT_NAME, 10, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2, sticky="w")

# Begin the mainloop to listen to events and keep window on the screen
window.mainloop()
