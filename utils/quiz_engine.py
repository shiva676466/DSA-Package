

def run_quiz(questions):
    if not questions:
        print("\nNo quiz available for this topic.")
        return

    score = 0

    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")

        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")

        try:
            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > len(q["options"]):
                print("Invalid choice ❌")
                continue

            selected_option = q["options"][choice - 1]

            if selected_option == q["answer"]:
                print("Correct ✅")
                score += 1
            else:
                print(f"Wrong ❌ (Correct: {q['answer']})")

        except ValueError:
            print("Please enter a valid number ❌")

    print(f"\nYour Final Score: {score}/{len(questions)}")