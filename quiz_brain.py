class QuizBrain:
    def __init__(self, qz_list):
        self.question_number = 0
        self.question_list = qz_list
        self.score = 0
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        question_n = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number}:{question_n.text} (True/False):")
        self.check_answer(user_answer,question_n.answer)
     
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You go it right!!")
            self.score +=1
            print(f"Your current score is : {self.score}/{self.question_number}.")
        elif self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was : {self.score}/{self.question_number}.")
        else:
            print("That's wrong")
            print(f"Te correct answer was : {correct_answer}")
            print(f"Your current score is : {self.score}/{self.question_number}.")
 