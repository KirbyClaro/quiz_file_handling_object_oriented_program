class QuizUI:
    """Handles all user interactions."""
    
    @staticmethod
    def get_filename() -> str:
        """Get filename from user with validation."""
        while True:
            filename = input("Enter the filename to save questions (default: quiz_questions.txt): ").strip()
            if filename:
                if not filename.endswith('.txt'):
                    filename += '.txt'
                return filename
            print("Filename cannot be empty!")
        return 'quiz_questions.txt'

    @staticmethod
    def get_question() -> str:
        """Get question from user with validation."""
        while True:
            question = input("Enter your question: ").strip()
            if question:
                return question
            print("Question cannot be empty!")

    @staticmethod
    def get_answers() -> list:
        """Get four possible answers from user."""
        answers = []
        for label in ['A', 'B', 'C', 'D']:
            while True:
                answer = input(f"Enter answer {label}: ").strip()
                if answer:
                    answers.append(answer)
                    break
                print(f"Answer {label} cannot be empty!")
        return answers

    @staticmethod
    def get_correct_answer() -> str:
        """Get correct answer from user."""
        while True:
            correct = input("Enter the correct answer (A/B/C/D): ").upper().strip()
            if correct in ['A', 'B', 'C', 'D']:
                return correct
            print("Invalid input! Please enter A, B, C, or D.")