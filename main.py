from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    qm_answer = i["correct_answer"]
    qm_text = i["question"]
    question_model = Question(qm_text,qm_answer)
    question_bank.append(question_model)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    