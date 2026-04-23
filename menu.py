from levels import select_level
from utils.quiz_engine import run_quiz
# load interview questions directly from questions.json
import random
from utils.ui import box_menu
import utils.ui as ui
import json
import os
import time
from datetime import datetime, timedelta

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


def get_all_questions():
    file_path = "data/questions.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except Exception:
        return []

    questions = []
    for key, value in data.items():
        if key.endswith("_quiz") and isinstance(value, list):
            questions.extend(value)
    return questions


def update_streak():
    file_path = "data/streak.json"
    today = datetime.now().date()

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except:
            data = {}
    else:
        data = {}

    last_opened = data.get("last_opened")
    streak = data.get("streak", 0)

    if last_opened:
        try:
            last_date = datetime.strptime(last_opened, "%Y-%m-%d").date()
        except:
            last_date = today
    else:
        last_date = today

    if last_opened is None:
        streak = 1
    elif today == last_date:
        pass
    elif today == last_date + timedelta(days=1):
        streak += 1
    else:
        streak = 1

    with open(file_path, "w") as file:
        json.dump({
            "last_opened": str(today),
            "streak": streak
        }, file, indent=4)

    return streak


def show_progress_chart():
    file_path = "data/progress.json"

    if not os.path.exists(file_path):
        print("\nNo progress data found.")
        input("\nPress Enter to return...")
        return

    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except:
            data = {}

    width = 50
    print("┏" + "━" * width + "┓")
    print("┃" + " PROGRESS CHART 📊 ".center(width) + "┃")
    print("┣" + "━" * width + "┫")

    if not data:
        print("┃" + "No progress yet.".center(width) + "┃")
    else:
        for topic, info in data.items():
            if isinstance(info, dict):
                percent = int(info.get("percentage", 0))
            else:
                # Support old progress.json format where values may be plain numbers
                percent = int(info) if str(info).isdigit() else 0

            if percent >= 80:
                color = GREEN
            elif percent >= 50:
                color = YELLOW
            else:
                color = RED

            max_bars = percent // 10
            for step in range(max_bars + 1):
                bars = color + ("█" * step) + RESET
                row = f"{topic.upper():12} {bars:<20} {percent}%"
                print("┃" + row.ljust(width) + "┃", end="\r")
                time.sleep(0.06)
            print("┃" + row.ljust(width) + "┃")

    print("┗" + "━" * width + "┛")
    input("\nPress Enter to return...")



def interview_mode():
    print("\n🎯 INTERVIEW MODE\n")
    print("You will get 5 random DSA questions.")
    print("Try to answer under pressure!\n")
    input("Press Enter to start...")

    try:
        questions = get_all_questions()
    except:
        print("Unable to load questions.")
        input("Press Enter to return...")
        return

    random.shuffle(questions)
    selected = questions[:5]
    run_quiz(selected, "interview")


# --- Search topic function ---
def search_topic():
    query = input("\nEnter topic name to search: ").strip().lower()

    topic_map = {
        "arrays": ("content.arrays", "arrays_content"),
        "array": ("content.arrays", "arrays_content"),
        "strings": ("content.strings", "strings_content"),
        "string": ("content.strings", "strings_content"),
        "stack": ("content.stacks", "stacks_content"),
        "stacks": ("content.stacks", "stacks_content"),
        "queue": ("content.queue", "queue_content"),
        "linked list": ("content.linked_list", "linked_list_content"),
        "linkedlist": ("content.linked_list", "linked_list_content"),
        "tree": ("content.trees", "trees_content"),
        "trees": ("content.trees", "trees_content"),
        "sorting": ("content.sorting", "sorting_content"),
        "searching": ("content.searching", "searching_content"),
        "graphs": ("content.graphs", "graphs_content"),
        "graph": ("content.graphs", "graphs_content"),
        "heap": ("content.heap", "heap_content"),
        "dp": ("content.dynamic_programming", "dynamic_programming_content"),
        "dynamic programming": ("content.dynamic_programming", "dynamic_programming_content"),
        "trie": ("content.trie", "trie_content"),
        "recursion": ("content.recursion", "recursion_content")
    }

    if query not in topic_map:
        print("Topic not found.")
        input("\nPress Enter to return...")
        return

    try:
        module_name, func_name = topic_map[query]
        module = __import__(module_name, fromlist=['*'])
        getattr(module, func_name)()
    except Exception:
        print("Unable to open topic.")
        input("\nPress Enter to return...")


# --- Theme selector function ---
def theme_selector():
    print("\n🎨 SELECT THEME\n")
    print("1. Default Blue")
    print("2. Hacker Green")
    print("3. Neon Purple")
    print("4. Fire Red")
    print("5. Light Mode")

    choice = input("\nEnter choice: ").strip()

    theme_map = {
        "1": "default",
        "2": "hacker",
        "3": "neon",
        "4": "fire",
        "5": "light"
    }

    if choice not in theme_map:
        print("Invalid choice.")
        input("\nPress Enter to return...")
        return

    os.makedirs("data", exist_ok=True)
    with open("data/theme.json", "w") as file:
        json.dump({"theme": theme_map[choice]}, file, indent=4)

    ui.apply_theme()
    print("\nTheme updated successfully! 🎉")
    input("\nPress Enter to return...")


def weak_topic_analyzer():
    file_path = "data/progress.json"

    if not os.path.exists(file_path):
        print("\nNo progress data found.")
        input("\nPress Enter to return...")
        return

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except:
        data = {}

    if not data:
        print("\nNo progress yet.")
        input("\nPress Enter to return...")
        return

    results = []
    for topic, info in data.items():
        if isinstance(info, dict):
            percent = int(info.get("percentage", 0))
        else:
            percent = int(info) if str(info).isdigit() else 0
        results.append((topic, percent))

    results.sort(key=lambda x: x[1])

    print("\n🧠 WEAK TOPIC ANALYZER\n")

    limit = min(3, len(results))
    for i in range(limit):
        topic, percent = results[i]
        print(f"{i+1}. {topic.upper():15} - {percent}%")

    weakest_topic = results[0][0]
    print(f"\nRecommendation: Practice {weakest_topic.upper()} today. 🎯")
    input("\nPress Enter to return...")


def main_menu():
    while True:
        streak = update_streak()
        box_menu(f"DSA PACKAGE ⚡  🔥 Streak: {streak} Day(s)", [
            ("1", "Start"),
            ("2", "Progress Chart 📊"),
            ("3", "Interview Mode 🎯"),
            ("4", "Search Topic 🔍"),
            ("5", "Themes 🎨"),
            ("6", "Weak Topic Analyzer 🧠"),
            ("7", "Exit")
        ])

        choice = input("Enter choice: ")

        if choice == '1':
            select_level()
        elif choice == '2':
            print()
            show_progress_chart()
        elif choice == '3':
            interview_mode()
        elif choice == '4':
            search_topic()
        elif choice == '5':
            theme_selector()
        elif choice == '6':
            weak_topic_analyzer()
        elif choice == '7':
            print("Exiting....!")
            break
        else:
            print("Invalid Choice, please enter valid option")
