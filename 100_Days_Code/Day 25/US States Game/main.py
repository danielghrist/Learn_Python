import turtle
import pandas

# Code to get the (x, y) values of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

WIDTH = 725
HEIGHT = 491
FILE_PATH = "./100_Days_Code/Day 25/US States Game/"

screen = turtle.Screen()
screen.title("U.S. States Guessing Game")
screen.setup(WIDTH, HEIGHT)
screen_writer = turtle.Turtle()
screen_writer.penup()
screen_writer.hideturtle()

image = f"{FILE_PATH}blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)
# turtle.shape(image)
state_data = pandas.read_csv(f"{FILE_PATH}50_states.csv")


# Code to pull x and y coordinates from the list of states DataFrame
def get_state_coors(player_guess):
    x = int(state_data[state_data.state == player_guess]["x"])
    y = int(state_data[state_data.state == player_guess]["y"])
    return (x, y)


# Write the state name the player entered onto the screen
def write_state_to_screen(turtle, player_guess):
    turtle.goto(get_state_coors(player_guess))
    turtle.write(arg=player_guess, align="center",
                 font=("Arial", 10, "normal"))


# Retun True if player's guess was in the DataFrame of states
def check_player_guess(player_guess, correct_guesses: list, df: pandas.DataFrame):
    states = df.state.to_list()
    for state in states:
        if player_guess == state and correct_guesses.count(state) == 0:
            return True
    return False


is_game_over = False
num_correct_answers = 0
total_states = 50
text_input_title = "Guess the State"
correct_answers = []


while not is_game_over:
    player_answer = screen.textinput(
        title=text_input_title, prompt="Guess the name of a state").title()

    if player_answer == "Exit":
        states = state_data.state.to_list()
        # List comprehension does the same thing as the commented out for loop below
        not_guessed_states = [
            state for state in states if state not in correct_answers]
        turtle.write(f"You guessed {num_correct_answers} out of {total_states} states.\n",
                     align="center", font=("Arial", 25, "bold"))
        turtle.write(f"The states you missed have been saved",
                     align="center", font=("Arial", 25, "bold"))
        with open("player_save_data.txt", "w") as file:
            # for state in states:
            #     if state not in correct_answers:
            #         not_guessed_states.append(state)
            new_data = pandas.DataFrame(not_guessed_states)
            file.write(f"{new_data}")
        break

    # Check if player correctly guessed a state
    # print(check_player_guess(player_answer, state_data))

    if check_player_guess(player_answer, correct_guesses=correct_answers, df=state_data):
        num_correct_answers += 1
        write_state_to_screen(screen_writer, player_answer)
        text_input_title = f"{num_correct_answers}/{total_states} Correct"
        correct_answers.append(player_answer)

    if num_correct_answers == 50:
        turtle.home()
        turtle.write("You guessed all the states.  You win!",
                     align="center", font=("Arial", 25, "bold"))
        is_game_over = True


turtle.mainloop()
