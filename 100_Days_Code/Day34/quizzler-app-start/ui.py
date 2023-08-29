from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Calibri", 20, "italic")


# NOTE TO SELF: YOU CAN CREATE A GUI IN A CLASS AND JUST INITIALIZE ALL THE ITEMS YOU NEED
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text=f"Score: 0")
        self.score_text.config(bg=THEME_COLOR, fg="white",
                               font=("Arial", 10, "bold"))
        self.score_text.grid(row=0, column=1, sticky="nes")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(
            150, 125, text="TEST", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_button_img, width=100, height=97, bg=THEME_COLOR, bd=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        self.false_button = Button(image=false_button_img, width=100, height=97, bg=THEME_COLOR, bd=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.update_score_text()
        if self.quiz.still_has_questions():
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            next_question = self.quiz.next_question()
            self.canvas.itemconfigure(self.q_text, text=next_question)
        else:
            self.canvas.itemconfigure(
                self.q_text, text=f"The Quiz Is Over! You Scored {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.right_wrong_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.right_wrong_feedback(self.quiz.check_answer("False"))

    def update_score_text(self):
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def right_wrong_feedback(self, is_answer_right):
        if is_answer_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, func=self.get_next_question)
