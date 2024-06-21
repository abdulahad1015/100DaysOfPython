from html import unescape

no_of_questions = 0
class Quiz_brain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_bank = q_list
        self.score = 0



    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        choice = input(unescape(f"Q.{self.question_number}: {current_question.text} (True/False): "))
        self.check_answer(choice, current_question.answer)
        print("\n")

    def still_has_question(self):
        if (self.question_number >=  no_of_questions):
            return False
        else:
            return True

    def check_answer(self, user_answer, question_answer):
        if (user_answer.lower() == question_answer.lower()):
            print("Correct !")
            self.score += 10
        else:
            print("Incorrect !")
        print("Score: ", self.score)

