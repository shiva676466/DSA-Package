import json
import os
import time
import requests
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

API_BASE = "http://127.0.0.1:8000"

try:
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_KEY_PATH)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception:
    db = None


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


def save_to_firebase(score, total, topic="general"):
    if db is None:
        print(f"{RED}Firebase not initialized.{RESET}")
        return

    try:
        percentage = round((score / total) * 100, 2) if total else 0
        db.collection("quiz_scores").add({
            "topic": topic,
            "score": score,
            "total": total,
            "percentage": percentage,
            "timestamp": datetime.now().isoformat()
        })
        print(f"{GREEN}Score saved to Firebase cloud ✅{RESET}")
    except Exception as e:
        print(f"{RED}Firebase save failed: {e}{RESET}")


# Save to backend API
def save_to_backend(score, total, topic="general", username="shiva"):
    try:
        payload = {
            "username": username,
            "topic": topic,
            "score": score,
            "total": total
        }
        response = requests.post(f"{API_BASE}/score", json=payload, timeout=3)
        if response.status_code == 200:
            print(f"{GREEN}Score synced to backend API ✅{RESET}")
        else:
            print(f"{RED}Backend sync failed.{RESET}")
    except Exception:
        print(f"{YELLOW}Backend offline. Saved locally only.{RESET}")


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


def run_quiz(questions, topic="general", timed=False, time_limit=20):
    if not questions:
        print("\nNo quiz available for this topic.")
        return

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        print()
        show_question_box(i, q['question'], q['options'])
        if timed:
            print(f"{YELLOW}⏱️ Time Limit: {time_limit} seconds{RESET}")

        while True:
            start_time = time.time()
            choice = input("Enter your choice: ").strip()
            if timed and (time.time() - start_time) > time_limit:
                print(f"{RED}Time's Up! ❌{RESET}")
                choice = "0"

            if not choice.isdigit():
                print(f"{RED}Please enter a valid number ❌{RESET}")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(q["options"]):
                print(f"{RED}Invalid choice ❌{RESET}")
                continue

            break

        selected_option = q["options"][choice - 1] if choice != 0 else None

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

        if i == total:
            input("Press Enter to go back...")
        else:
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
    save_to_firebase(score, total, topic)
    save_to_backend(score, total, topic)