from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.Score_Label=Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",14,"bold"))
        self.Score_Label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.question_text=self.canvas.create_text(150,125,text="Question",fill=THEME_COLOR,font=("Arial",20,"italic"))

        true_img=PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.button1=Button(image=false_img)
        self.button1.grid(row=2,column=0)
        self.button2 = Button(image=true_img)
        self.button2.grid(row=2, column=1)

        self.window.mainloop()
a=QuizInterface()
