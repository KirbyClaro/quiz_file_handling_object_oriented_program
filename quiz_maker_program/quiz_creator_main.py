from data_manager import DataManager
from quiz_ui import QuizUI

class QuizManager:
    """Main class coordinating quiz creation."""
    
    def __init__(self):
        """Initialize quiz manager with UI and data manager."""
        self.filename = QuizUI.get_filename()
        print(f"Questions will be saved to: {self.filename}")
        self.data_manager = DataManager(self.filename)

    def start_quiz_creation(self):
        """Manage the process of adding questions to the quiz."""
        print("~~~~~~~~Welcome to Quiz Creator!~~~~~~~~")
        print("Press Control + C to quit.")
        
        while True:
            question = QuizUI.get_question()
            answers = QuizUI.get_answers()
            correct_answer = QuizUI.get_correct_answer()
            
            self.data_manager.save_question(question, answers, correct_answer)
            print("Question saved successfully!")
            
            cont = input("\nWould you like to add another question? (yes/no): ").lower()
            if cont != 'yes':
                break
        
        print("\nThank you for using Quiz Creator!")
        print("\nI hope you liked it! :D")

if __name__ == "__main__":
    quiz_manager = QuizManager()
    quiz_manager.start_quiz_creation()