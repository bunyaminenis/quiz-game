class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {current_question.text}\nIs that True or False? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Answer is right")
            self.score += 1
        else:
            print("Answer is wrong")
            print(f"Correct answer was: {correct_answer}")
        print(f"{self.score}/ {self.question_number}")
        print("\n")
