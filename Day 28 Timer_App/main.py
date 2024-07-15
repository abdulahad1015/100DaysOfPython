from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reset = False
clock_running = False
check_string=""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reset,check_string,reps
    reset = True
    canvas.itemconfig(timer_text, text="00:00")
    check_string = ""
    check_marks.config(text=check_string)
    reps=0
    canvas.itemconfig(text, text=f"Timer", fill=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, reset, clock_running
    reset = False
    if (clock_running == True and reps == 0):
        return
    clock_running = True
    if (reps % 8 == 0 and reps!=0):
        canvas.itemconfig(text, text=f"Break", fill=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif (reps % 2 == 0):
        canvas.itemconfig(text, text=f"Work", fill=GREEN)
        count_down(WORK_MIN * 60)
    else:
        canvas.itemconfig(text, text=f"Break", fill=PINK)
        count_down(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global check_string
    if (reset == True):
        return
    mins = int(count / 60)
    seconds = int(count % 60)
    if (seconds == 0):
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")
    if count >= 0:
        window.after(1000, count_down, count - 1)
    else:
        # window.after_cancel(a)
        reps += 1
        if(reps%2==0):
            check_string= check_string + "✔"
            check_marks.config(text=check_string)
        if(reps==9):
            reset_timer()
        start_timer()
        return


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
fg = GREEN

canvas = Canvas(width=250, height=300, bg=YELLOW, highlightthickness=0)
canvas.create_image(123, 150, image=tomato_img)
timer_text = canvas.create_text(125, 160, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.pack()
text = canvas.create_text(130, 20, text="Timer", fill=GREEN, font=(FONT_NAME, 32, "bold"))

Start = Button(text=" Start ", width=7, command=start_timer)
Start.place(x=0, y=270)

Reset = Button(text="Reset", width=7, command=reset_timer)
Reset.place(x=185, y=270)

check_marks = Label(fg=GREEN, bg=YELLOW, font={FONT_NAME, 20, "bold"})
check_marks.place(x=85, y=270)

window.mainloop()
