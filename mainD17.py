from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Create the question bank:
#   Write a loop iterating over the question_data. Create a Question object from each entry in question_data/
#   Append each Question object to the question_bank

question_bank = []


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz. \nYour final score was: {quiz.score} / {len(question_bank)}")
