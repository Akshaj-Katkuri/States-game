import turtle
import pandas as pd


window = turtle.Screen()
window.title('US States Game')

# variables
image = 'blank_states_img.gif'
guess_states = []
missing_states = []

window.addshape(image)
turtle.shape(image)

# setting database
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

def check_guess():
    if state_guess in all_states:
        guess_states.append(state_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == state_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_guess)
    elif state_guess == 'Exit':
        for i in all_states:
            if i not in guess_states:
                missing_states.append(i)
        newdata = pd.DataFrame(missing_states)
        newdata.to_csv("states to learn.csv")

# function used for finding the coordinates of a position with just a click
def click_coor(x,y):
    print(x,y)

turtle.onscreenclick(click_coor)

while True:
    state_guess = window.textinput(title=f" {50-(len(guess_states))}/50 left", prompt='Enter a US State Name').title()
    check_guess()
    if state_guess == 'Exit':
        break
