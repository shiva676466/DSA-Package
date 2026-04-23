import os
import json

# Default theme colors
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"


def load_theme():
    file_path = "data/theme.json"
    if not os.path.exists(file_path):
        return "default"

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data.get("theme", "default")
    except:
        return "default"


def apply_theme():
    global BLUE, GREEN, YELLOW, CYAN

    theme = load_theme()

    if theme == "hacker":
        BLUE = "\033[92m"
        GREEN = "\033[92m"
        YELLOW = "\033[97m"
        CYAN = "\033[92m"

    elif theme == "neon":
        BLUE = "\033[95m"
        GREEN = "\033[96m"
        YELLOW = "\033[93m"
        CYAN = "\033[95m"

    elif theme == "fire":
        BLUE = "\033[91m"
        GREEN = "\033[93m"
        YELLOW = "\033[97m"
        CYAN = "\033[91m"

    elif theme == "light":
        BLUE = "\033[97m"
        GREEN = "\033[94m"
        YELLOW = "\033[95m"
        CYAN = "\033[96m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def line(width=50):
    return "━" * width


def box_menu(title, options):
    apply_theme()
    clear()

    width = 50

    print(f"{BLUE}┏{line(width)}┓{RESET}")
    print(f"{BLUE}┃{YELLOW}{title.center(width)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣{line(width)}┫{RESET}")

    for key, value in options:
        text = f"[{key}] {value}"
        print(f"{BLUE}┃ {GREEN}{text.ljust(width-1)}{BLUE}┃{RESET}")

    print(f"{BLUE}┗{line(width)}┛{RESET}")