from D17_question_model import  Question
from D17_data import question_data
from D17_quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz\n"
      f"Your final score is: {quiz.score}/{len(quiz.question_list)}")

