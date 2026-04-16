import os

BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def line(width=50):
    return "━" * width


def box_menu(title, options):
    clear()

    width = 50

    print(f"{BLUE}┏{line(width)}┓{RESET}")
    print(f"{BLUE}┃{YELLOW}{title.center(width)}{BLUE}┃{RESET}")
    print(f"{BLUE}┣{line(width)}┫{RESET}")

    for key, value in options:
        text = f"[{key}] {value}"
        print(f"{BLUE}┃ {GREEN}{text.ljust(width-1)}{BLUE}┃{RESET}")

    print(f"{BLUE}┗{line(width)}┛{RESET}")