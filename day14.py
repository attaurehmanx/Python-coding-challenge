def quiz():
    score = 0

    questions = [
        {
            "question": "1. What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "2. Which language is used for web apps?",
            "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
            "answer": "C"
        },
        {
            "question": "3. What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
            "answer": "B"
        },
        {
            "question": "4. Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "C"
        },
        {
            "question": "5. Who wrote 'Hamlet'?",
            "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
            "answer": "B"
        }
    ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user == q["answer"]:
            print("Right answer")
            score += 1
        else:
            print(f"wrong answer the right answer is {q["answer"]}")

    print(f"your final score is {score}")

quiz()