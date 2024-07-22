from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def Result(self,is_correct):

        if(is_correct):
            print("1")
            self.canvas.config(bg="green")
            self.window.after(1000,self.get_next_question)

        else:
            print("0")
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)


    def true(self):
        is_correct=self.quiz.check_answer("True")
        self.Result(is_correct)
        # time.sleep(1)


    def false(self):
        is_correct=self.quiz.check_answer("False")
        self.Result(is_correct)
        # time.sleep(1)

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.Score_Label=Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",14,"bold"))
        self.Score_Label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.question_text=self.canvas.create_text(150,125,text="Question",fill=THEME_COLOR,font=("Arial",18,"italic"),width=280)
        self.get_next_question()

        true_img=PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.button1=Button(image=false_img, command=self.true)
        self.button1.grid(row=2,column=0)
        self.button2 = Button(image=true_img,command=self.false)
        self.button2.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=f"Q{self.quiz.question_number}: {q_text}")
        self.Score_Label.config(text=f"Score: {self.quiz.score}")


