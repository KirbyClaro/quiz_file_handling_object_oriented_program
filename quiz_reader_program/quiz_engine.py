import random
from utils import get_user_answer
from question_loader import QuestionLoader

class QuizGame:
    def __init__(self, filename: str):
        """Initialize the quiz game with questions from the file."""
        self.questions = QuestionLoader.load_questions(filename)

    def display_question(self, question_data: dict):
        """Displays a quiz question with answer choices."""
        print("\n" + "=" * 50)
        print(f"Question:\n{question_data['question']}")
        print(f"A. {question_data['A']}")
        print(f"B. {question_data['B']}")
        print(f"C. {question_data['C']}")
        print(f"D. {question_data['D']}")
        print("=" * 50)

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        """Checks if the user's answer is correct."""
        return user_answer == correct_answer

    def run_quiz(self):
        """Runs the quiz by randomly selecting questions."""
        if not self.questions:
            print("No questions found in the file.")
            return

        score = 0
        total = 0
        random.shuffle(self.questions)

        for question in self.questions:
            self.display_question(question)
            user_answer = get_user_answer()
            if self.check_answer(user_answer, question["correct"]):
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {question['correct']}.\n")
            total += 1

        print("=" * 50)
        print(f"🎯 You got {score} out of {total} correct.")
        print("=" * 50)