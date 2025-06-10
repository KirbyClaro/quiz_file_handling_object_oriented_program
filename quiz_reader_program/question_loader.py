class QuestionLoader:
    @staticmethod
    def load_questions(filename: str) -> list:
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