import pandas
import turtle as t

#will have to be edited if ran from the repo
IMAGE = r"Day25\StatesGame\blank_states_img.gif"
FONT = ("Mighty Souly", 10, "normal")
VICTORY_FONT = ("Mighty Souly", 20, "bold")

screen = t.Screen()
screen.setup(780, 550)
screen.title("U.S States Game")
screen.addshape(IMAGE)
t.shape(IMAGE)

pen = t.Turtle(visible=False)
pen.penup()

STATE_DATA = pandas.read_csv(r"Day25\StatesGame\50_states.csv")
STATES = STATE_DATA.state.to_list()

def find_state_pos(state):
    state_index = STATE_DATA[STATE_DATA.state == state]
    state_x = int(state_index.x)
    state_y = int(state_index.y)

    return (state_x, state_y - 10)

def place_state(state):
    pen.goto(find_state_pos(state))
    pen.write(arg=state, align="center", font=FONT)

def output_missed_states(guessed_states, total_states):
    missed_states = []
    for state in total_states:
        if state not in guessed_states:
            missed_states.append(state)

    data = pandas.DataFrame(missed_states)
    data.to_csv("Day25\StatesGame\states_to_learn.csv")


guessed_states = []
completed = False
while not completed:
    state_select = screen.textinput(title=f"States guessed: {len(guessed_states)}/50", prompt="Start guessing states:")
    if state_select.title() in STATES and not state_select.title() in guessed_states:
        guessed_states.append(state_select.title())
        place_state(state=state_select.title())
    
    #                               debugger
    if len(guessed_states) == 50 or state_select == "50":
        pen.goto(0, 0)
        pen.color("blue")
        pen.write(arg="YOU GUESSED ALL 50 STATES!", align="center", font=VICTORY_FONT)
        completed = True


    if state_select == "quit":
        output_missed_states(guessed_states=guessed_states, total_states=STATES)
        exit()


screen.exitonclick()