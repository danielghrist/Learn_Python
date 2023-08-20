from turtle import Turtle
from datetime import datetime
from pathlib import Path
import os

X_POSITION = 0
Y_POSITION = 270
ALIGNMENT = "center"
FONT = ("Helvetica", 20, "bold")
REL_FILE_PATH = Path(__file__, "../").resolve()
SCORE_FILE = "highscores.txt"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("orange")
        # self.goto(X_POSITION, Y_POSITION)
        self.high_score = 0
        self.retrieve_highscore()
        self.update_scoreboard(0.1)

    # *** SPEED IS ONLY FOR DEBUGGING, NEED TO REMOVE AFTER ADDING EVERYTHING!!! ***
    def update_scoreboard(self, speed=float):
        '''Repositions the Turtle pen to write the current score, and highscore at a height relative to the window height.'''
        self.clear()
        self.penup()
        self.goto(x=X_POSITION, y=self.getscreen().window_height() / 2 - 35)
        self.write(
            f"Speed: {speed:3.3f} | Score: {self.score:02,} | High Score: {self.high_score:04,}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''Increases the scores by 1.'''
        self.score += 1

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(REL_FILE_PATH.joinpath(SCORE_FILE), "w") as file:
                file.write(f"{datetime.now()}: {self.high_score}")
                file.close()

    def reset(self):
        self.update_high_score()
        self.score = 0
        self.update_scoreboard(0.1)

    def retrieve_highscore(self):
        '''
        If file doesn't exist then set high_score to 0.
        If highscore file does exist then read and set the highscore to be
        displayed at the top of the game screen.
        '''
        if not REL_FILE_PATH.joinpath(SCORE_FILE).exists():
            self.high_score = 0
        else:
            with open(REL_FILE_PATH.joinpath(SCORE_FILE), "r") as file:
                contents = file.read()
                high_score = ''
                for char in range(contents.rfind(" ") + 1, len(contents), 1):
                    high_score += contents[char]

                self.high_score = int(high_score)
                file.close()
