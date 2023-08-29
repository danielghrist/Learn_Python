from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text, answer = question.items()
    question_bank.append(Question(question_text[1], answer[1]))

# print(question_bank[0].question_text)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("There are no more questions, you have completed the Quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
