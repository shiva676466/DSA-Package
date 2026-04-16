import json
import os


def save_progress(score, total):
    os.makedirs("data", exist_ok=True)
    data = {
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100, 2) if total else 0
    }

    with open("data/progress.json", "w") as file:
        json.dump(data, file, indent=4)



def run_quiz(questions):
    if not questions:
        print("\nNo quiz available for this topic.")
        return

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")

        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")

        while True:
            choice = input("Enter your choice: ").strip()

            if not choice.isdigit():
                print("Please enter a valid number ❌")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(q["options"]):
                print("Invalid choice ❌")
                continue

            break

        selected_option = q["options"][choice - 1]

        if selected_option == q["answer"]:
            print("Correct ✅")
            score += 1
        else:
            print(f"Wrong ❌ (Correct: {q['answer']})")

    percentage = round((score / total) * 100, 2)

    print("\n" + "=" * 35)
    print(f"Your Final Score: {score}/{total}")
    print(f"Percentage: {percentage}%")
    print("=" * 35)

    save_progress(score, total)