questions = [
    {
        "question": "What is the capital of India?",
        "answer": "delhi"
    },

    {
        "question": "Which language is used for Machine Learning?",
        "answer": "python"
    },

    {
        "question": "How many continents are there?",
        "answer": "7"
    },

    {
        "question": "Which planet is known as Red Planet?",
        "answer": "mars"
    }
]

score = 0

print("===== QUIZ APPLICATION =====")

for q in questions:

    user_answer = input(f"\n{q['question']} ").lower()

    if user_answer == q['answer']:

        print("Correct!")

        score += 1

    else:

        print("Wrong Answer")

print(f"\nFinal Score: {score}/{len(questions)}")