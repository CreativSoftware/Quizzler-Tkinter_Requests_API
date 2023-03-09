from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler".center(25))
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_text = Label(text=f"Score: {self.score}", font=("Arial", 15, "bold"), background=THEME_COLOR, foreground="white")
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, padx=10, pady=10, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, padx=10, pady=10, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()

    
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the Quiz. Your score is {self.score} out of 10")
            self.true_button.destroy()
            self.false_button.destroy()

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct == True:
            self.score += 1
            self.canvas.config(background="green")
            self.score_text.config(text=f"Score: {self.score}")
            self.window.after(2000, self.get_next_question)
            
            
        elif is_correct == False:
            self.canvas.config(background="red")
            self.window.after(2000, self.get_next_question)
            
            
