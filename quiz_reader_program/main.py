from utils import prompt_filename
from quiz_engine import QuizGame

def main():
    filename = prompt_filename()
    game = QuizGame(filename)

    while True:
        game.run_quiz()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()