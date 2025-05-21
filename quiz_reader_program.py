#Create the Quiz program that read the output file of the Quiz Creator. 
#The user will answer the randomly selected 
#question and check if the answer is correct.


import random

#ask user for file name
class QuizGame:

    def __init__(self):
        """Initialize the quiz game with a filename."""
        self.filename = self.get_filename()
        self.questions = self.load_questions(self.filename)

    def get_filename(self) -> str:
        while True:
            filename = input("Enter the filename to load questions: ").strip()
            if filename:
                if not filename.endswith(".txt"):
                    filename += ".txt"
                return filename
            print("Filename cannot be empty!")

#access the file and read it
    def load_questions(self, filename: str) -> list:
        """Loads questions from a file and returns a list of question dictionaries."""
        questions = []
        try:
            with open(filename, "r") as file:
                content = file.read().strip().split("---\n")
                for block in content:
                    if block.strip() == "":
                        continue
                    lines = block.strip().split("\n")
                    question_data = {}
                    for line in lines:
                        if line.startswith("QUESTION:"):
                            question_data["question"] = line[len("QUESTION:"):].strip()
                        elif line.startswith("A:"):
                            question_data["A"] = line[2:].strip()
                        elif line.startswith("B:"):
                            question_data["B"] = line[2:].strip()
                        elif line.startswith("C:"):
                            question_data["C"] = line[2:].strip()
                        elif line.startswith("D:"):
                            question_data["D"] = line[2:].strip()
                        elif line.startswith("CORRECT:"):
                            question_data["correct"] = line[len("CORRECT:"):].strip()
                    if question_data:
                        questions.append(question_data)
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found.")
        return questions

#display the questions
    def display_question(self, question_data: dict):
        """Displays a quiz question with answer choices."""
        print("\n" + "="*50)
        print(f"Question:")
        print(question_data["question"])
        print(f"A. {question_data['A']}")
        print(f"B. {question_data['B']}")
        print(f"C. {question_data['C']}")
        print(f"D. {question_data['D']}")
        print("="*50)
    
#accept and check user answer
    def get_user_answer(self) -> str:
        """Gets the user's answer and ensures it's valid."""
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("Invalid input. Please enter A, B, C, or D.")

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        """Checks if the user's answer is correct."""
        return user_answer == correct_answer

#run quiz and score
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
            user_answer = self.get_user_answer()
            if self.check_answer(user_answer, question["correct"]):
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {question['correct']}.\n")
            total += 1

        print("="*50)
        print(f"🎯 You got {score} out of {total} correct.")
        print("="*50)
    
#main function with replay option
    def start_game(self):
        """Starts the quiz game and allows replaying."""
        while True:
            self.run_quiz()
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thanks for playing!")
                break
        
if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.start_game()
