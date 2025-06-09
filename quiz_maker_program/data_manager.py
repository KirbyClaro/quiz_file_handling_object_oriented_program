class DataManager:
    """Handles quiz data persistence."""
    
    def __init__(self, filename):
        """Initialize with a filename."""
        self.filename = filename
        
    def save_question(self, question: str, answers: list, correct_answer: str):
        """Save a question and its answers to file."""
        with open(self.filename, "a") as file:
            file.write(f"QUESTION:{question}\n")
            file.write(f"A:{answers[0]}\n")
            file.write(f"B:{answers[1]}\n")
            file.write(f"C:{answers[2]}\n")
            file.write(f"D:{answers[3]}\n")
            file.write(f"CORRECT:{correct_answer}\n")
            file.write("---\n")