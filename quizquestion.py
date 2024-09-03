questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "correct_answer": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": 2
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
        "correct_answer": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": 4
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Au", "Hg", "Pb"],
        "correct_answer": 2
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["Blue whale", "Fin whale", "Humpback whale", "Sperm whale"],
        "correct_answer": 1
    }
]

score = 0

for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    answer = int(input("Your answer (1-4): "))
    if answer == q["correct_answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

print(f"Your final score is {score} out of {len(questions)}")
