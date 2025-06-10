def prompt_filename() -> str:
    """Prompt the user to enter a filename for loading quiz questions."""
    while True:
        filename = input("Enter the filename to load questions: ").strip()
        if filename:
            if not filename.endswith(".txt"):
                filename += ".txt"
            return filename
        print("Filename cannot be empty!")

def get_user_answer() -> str:
    """Gets the user's answer and ensures it's valid."""
    while True:
        answer = input("Your answer (A/B/C/D): ").upper().strip()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("Invalid input. Please enter A, B, C, or D.")