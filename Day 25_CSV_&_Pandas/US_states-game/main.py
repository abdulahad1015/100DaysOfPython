import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
name_draw = turtle.Turtle(visible=False)
name_draw.penup()
name_draw.speed(0)

data = pandas.read_csv("50_states.csv")

not_guessed=[]
all_states=data.state.tolist()
score=0
guessed_states=[]

while(score<50):
    answer_state = screen.textinput(title=f"{score} / 50", prompt="Whats another State ?")
    answer_state=answer_state.title()
    state = data[data["state"] == answer_state]
    if(answer_state=="Exit"):
        not_guessed=[i for i in all_states if i not in guessed_states]
        new_data=pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn.csv")

        print(not_guessed)
        break
    if(len(state)==0 or answer_state in guessed_states):
        continue

    score+=1
    guessed_states.append(answer_state) 
    x = state.iloc[0].x
    y = state.iloc[0].y
    name_draw.goto(x,y)
    name_draw.dot()
    name_draw.write(arg=answer_state,font=("Arial",7,"normal"))

