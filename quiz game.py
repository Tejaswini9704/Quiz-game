import time

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
                "answer": 3
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
                "answer": 2
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["1. Charles Dickens", "2. William Shakespeare", "3. Jane Austen", "4. Mark Twain"],
                "answer": 2
            }
        ]
        self.score = 0

    def start_game(self):
        print("Welcome to the Quiz Game!\n")
        time.sleep(1)

        for q in self.questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = int(input("\nEnter the number of your answer: "))
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print("Wrong! The correct answer was", q["options"][q["answer"] - 1], "\n")
            time.sleep(1)

        print(f"Game Over! Your final score: {self.score}/{len(self.questions)}")

# Run the quiz game
quiz = QuizGame()
quiz.start_game()
