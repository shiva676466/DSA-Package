import json
import os
import time

# ANSI color constants
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


def save_progress(score, total, topic="general"):
    os.makedirs("data", exist_ok=True)
    file_path = "data/progress.json"

    percentage = round((score / total) * 100, 2) if total else 0

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
            except:
                data = {}
    else:
        data = {}

    data[topic] = {
        "score": score,
        "total": total,
        "percentage": percentage
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)



def show_question_box(number, question, options):
    width = 70
    print(f"{BLUE}┏" + "━" * width + f"┓{RESET}")
    print(f"{BLUE}┃{YELLOW}{(' Question ' + str(number)).center(width)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣" + "━" * width + f"┫{RESET}")
    print(f"{BLUE}┃ {question.ljust(width-1)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣" + "━" * width + f"┫{RESET}")
    for i, opt in enumerate(options, start=1):
        row = f"[{i}] {opt}"
        print(f"{BLUE}┃ {GREEN}{row.ljust(width-1)}{BLUE}┃{RESET}")
    print(f"{BLUE}┗" + "━" * width + f"┛{RESET}")


def run_quiz(questions, topic="general"):
    if not questions:
        print("\nNo quiz available for this topic.")
        return

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        print()
        show_question_box(i, q['question'], q['options'])

        while True:
            choice = input("Enter your choice: ").strip()

            if not choice.isdigit():
                print(f"{RED}Please enter a valid number ❌{RESET}")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(q["options"]):
                print(f"{RED}Invalid choice ❌{RESET}")
                continue

            break

        selected_option = q["options"][choice - 1]

        if selected_option == q["answer"]:
            print(f"{GREEN}Correct ✅{RESET}")
            score += 1
        else:
            print(f"{RED}Wrong ❌{RESET} {YELLOW}(Correct: {q['answer']}){RESET}")

        explanation = q.get("explanation")
        if explanation:
            print(f"{CYAN}Explanation:{RESET} {explanation}")
        else:
            print(f"{CYAN}Explanation:{RESET} The correct answer is {q['answer']} based on the concept being tested.")

        input("Press Enter for next question...")

    percentage = round((score / total) * 100, 2)

    print()
    print(f"{BLUE}┏" + "━" * 35 + f"┓{RESET}")
    print(f"{BLUE}┃{YELLOW}{' QUIZ RESULT 🏆 '.center(35)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣" + "━" * 35 + f"┫{RESET}")
    print(f"{BLUE}┃ {GREEN}{('Score: ' + str(score) + '/' + str(total)).ljust(34)}{BLUE}┃{RESET}")
    print(f"{BLUE}┃ {CYAN}{('Percentage: ' + str(percentage) + '%').ljust(34)}{BLUE}┃{RESET}")
    print(f"{BLUE}┗" + "━" * 35 + f"┛{RESET}")

    save_progress(score, total, topic)