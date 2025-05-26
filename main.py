import turtle
import pandas as pd


window = turtle.Screen()
window.title('US States Game')

# variables
image = 'blank_states_img.gif'
guess_states = [] # States that have been guessed
missing_states = [] # States that user didn't manage to get

window.addshape(image)
turtle.shape(image)

# setting database
data = pd.read_csv('50_states.csv') 
all_states = data.state.to_list()

def check_guess(guess):
    if guess in all_states:
        guess_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
    elif guess == 'Exit':
        for i in all_states:
            if i not in guess_states:
                missing_states.append(i)

# function used for finding the coordinates of a position with just a click
def click_coor(x,y):
    print(x,y)

turtle.onscreenclick(click_coor)

while True:
    state_guess = window.textinput(
        title=f"{50 - len(guess_states)}/50 States Remaining",
        prompt="Enter a US State Name"
    ).title()
    check_guess(state_guess)
    if state_guess == 'Exit':
        print("States to learn: ")
        for i in missing_states: 
            print(i)
        break
