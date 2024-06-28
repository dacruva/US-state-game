import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=700, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
text = turtle.Turtle

states_csv = pd.read_csv("50_states.csv")

states = states_csv.state.values

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name").title()
    compare = answer_state in states
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state is not guessed_states:
                missing_states.append(state)
        list_remaining_states = pd.DataFrame(missing_states)
        list_remaining_states.to_csv("States_to_learn.csv")
        break

    if compare:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_csv[states_csv.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
