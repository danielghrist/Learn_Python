from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/MCKQEmHkUyGf6/giphy.gif?cid=ecf05e47609on1p3ic752bhcvlu9lytc1qhwn7wmc1j3p82d&rid=giphy.gif&ct=g' width=1000 alt='awesome-to-the-max'>"


@app.route("/bye")
@make_bold
@make_italic
@make_underline
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
