from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"


# ------------------------------------Read CSV----------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")


# ------------------------------------Get Card---------------------------------#
def next_card():
    global current_card,after_id
    window.after_cancel(after_id)
    try:
        current_card = random.choice(data_dict)
        canvas.itemconfig(word_text, text=current_card['French'])
    except IndexError:
        canvas.itemconfig(title_text, text="Fin")
        canvas.itemconfig(word_text, text="All words Learned")
    except KeyError:
        canvas.itemconfig(title_text, text="Fin")
        canvas.itemconfig(word_text, text="All words Learned")
    else:
        canvas.itemconfig(canvas_img, image=front_img)
        canvas.itemconfig(title_text, text="French")
        after_id = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_img,image=back_img)
    canvas.itemconfig(title_text,text="English")
    canvas.itemconfig(word_text,text=current_card['English'])

def is_known():
    data_dict.remove(current_card)
    to_learn=pandas.DataFrame(data_dict)
    to_learn.to_csv("data/words_to_learn.csv")
    next_card()

# ---------------------------------UI------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

after_id=window.after(3000,flip_card)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img=canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
next_card()

right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


window.mainloop()
