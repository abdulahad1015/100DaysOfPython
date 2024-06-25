import quiz_brain
from question_model import Question
from quiz_brain import Quiz_brain
import requests
from html import unescape

print(unescape("&gt;"))
question_bank = []
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")


response_data = response.json()
if response_data["response_code"] != 0:
    print("API Connection Failed")
    exit(0)
response_data = response_data["results"]

for i in response_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))
    quiz_brain.no_of_questions+=1

Quiz_brain = Quiz_brain(question_bank)

while Quiz_brain.still_has_question():
    Quiz_brain.next_question()

