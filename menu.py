from levels import select_level
from utils.ui import box_menu
import json
import os
import time

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


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



def main_menu():
    while True:
        box_menu("DSA PACKAGE ⚡", [
            ("1", "Start"),
            ("2", "Progress Chart 📊"),
            ("3", "Exit")
        ])

        choice = input("Enter choice: ")

        if choice == '1':
            select_level()
        elif choice == '2':
            print()
            show_progress_chart()
        elif choice == '3':
            print("Exiting....!")
            break
        else:
            print("Invalid Choice, please enter valid option")
