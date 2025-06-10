import time

# Questions data structure
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Mark Twain", "B. Charles Dickens", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    total_questions = len(quiz_questions)

    print("🎯 Welcome to the Quiz Game!\n")
    time.sleep(1)

    for idx, item in enumerate(quiz_questions):
        print(f"Question {idx + 1}: {item['question']}")
        for option in item['options']:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == item['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {item['answer']}.\n")

        time.sleep(1)

    print("📝 Quiz Completed!")
    print(f"Your final score is {score} out of {total_questions}.")
    if score == total_questions:
        print("🏆 Excellent! You're a quiz master.")
    elif score >= total_questions // 2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📚 Don't worry, try again and you'll improve!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()BaseException