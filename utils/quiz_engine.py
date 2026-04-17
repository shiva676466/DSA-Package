import json
import os
import time

# Firebase and datetime imports
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# ANSI color constants
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Firebase initialization
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIREBASE_KEY_PATH = os.path.join(BASE_DIR, "firebase-key.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_KEY_PATH)
    firebase_admin.initialize_app(cred)

db = firestore.client()


def save_progress(score, total):
    os.makedirs("data", exist_ok=True)
    data = {
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100, 2) if total else 0
    }

    with open("data/progress.json", "w") as file:
        json.dump(data, file, indent=4)


# Save to Firebase cloud
def save_to_firebase(score, total):
    try:
        percentage = round((score / total) * 100, 2) if total else 0

        db.collection("quiz_scores").add({
            "score": score,
            "total": total,
            "percentage": percentage,
            "timestamp": datetime.now().isoformat()
        })

        print(f"{GREEN}Score saved to Firebase cloud ✅{RESET}")
    except Exception as e:
        print(f"{RED}Firebase save failed: {e}{RESET}")



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


def run_quiz(questions):
    if not questions:
        print("\nNo quiz available for this topic.")
        return

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        print()
        show_question_box(i, q['question'], q['options'])
        print()
        show_question_box(i, q['question'], q['options'])

        while True:
            choice = input("Enter your choice: ").strip()

            if not choice.isdigit():
                print(f"{RED}Please enter a valid number ❌{RESET}")
                print(f"{RED}Please enter a valid number ❌{RESET}")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(q["options"]):
                print(f"{RED}Invalid choice ❌{RESET}")
                print(f"{RED}Invalid choice ❌{RESET}")
                continue

            break

        selected_option = q["options"][choice - 1]

        if selected_option == q["answer"]:
            print(f"{GREEN}Correct ✅{RESET}")
            print(f"{GREEN}Correct ✅{RESET}")
            score += 1
        else:
            print(f"{RED}Wrong ❌{RESET} {YELLOW}(Correct: {q['answer']}){RESET}")
            print(f"{RED}Wrong ❌{RESET} {YELLOW}(Correct: {q['answer']}){RESET}")

    percentage = round((score / total) * 100, 2)

    print()
    print(f"{BLUE}┏" + "━" * 35 + f"┓{RESET}")
    print(f"{BLUE}┃{YELLOW}{' QUIZ RESULT 🏆 '.center(35)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣" + "━" * 35 + f"┫{RESET}")
    print(f"{BLUE}┃ {GREEN}{('Score: ' + str(score) + '/' + str(total)).ljust(34)}{BLUE}┃{RESET}")
    print(f"{BLUE}┃ {CYAN}{('Percentage: ' + str(percentage) + '%').ljust(34)}{BLUE}┃{RESET}")
    print(f"{BLUE}┗" + "━" * 35 + f"┛{RESET}")
    print()
    print(f"{BLUE}┏" + "━" * 35 + f"┓{RESET}")
    print(f"{BLUE}┃{YELLOW}{' QUIZ RESULT 🏆 '.center(35)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣" + "━" * 35 + f"┫{RESET}")
    print(f"{BLUE}┃ {GREEN}{('Score: ' + str(score) + '/' + str(total)).ljust(34)}{BLUE}┃{RESET}")
    print(f"{BLUE}┃ {CYAN}{('Percentage: ' + str(percentage) + '%').ljust(34)}{BLUE}┃{RESET}")
    print(f"{BLUE}┗" + "━" * 35 + f"┛{RESET}")

    save_progress(score, total)
    save_to_firebase(score, total)