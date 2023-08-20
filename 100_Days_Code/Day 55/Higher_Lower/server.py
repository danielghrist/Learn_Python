from flask import Flask
import random

app = Flask(__name__)
COMP_GUESS = random.randint(0, 9)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9.</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:user_guess>")
def check_guess(user_guess):
    if user_guess > COMP_GUESS:
        return f"<p style='background-color: red'>Your guess of {user_guess} was too high.  Please guess a lower number</p>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif user_guess < COMP_GUESS:
        return f"<p>Your guess of {user_guess} was too low.  Please guess a higher number</p>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    else:
        return f"<p>Your guess of {user_guess} was correct!!  The computer number was {COMP_GUESS}</p>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
    
