from menu import main_menu
import time
import os

# ANSI color constants
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")



def type_text(text, color=RESET, delay=0.05):
    for ch in text:
        print(f"{color}{ch}{RESET}", end="", flush=True)
        time.sleep(delay)
    print()

def loading_screen():
    clear()
    print(f"{BLUE}" + "=" * 50 + f"{RESET}")
    type_text("        WELCOME TO DSA PACKAGE ⚡", YELLOW, 0.04)
    print(f"{BLUE}" + "=" * 50 + f"{RESET}")
    print(f"\n{CYAN}Loading...{RESET}")

    bar = ""
    for _ in range(20):
        bar += "█"
        print(f"\r{GREEN}[{bar:<20}]{RESET}", end="")
        time.sleep(0.08)

    print(f"\n\n{YELLOW}Ready to Launch 🚀{RESET}")
    time.sleep(1)
    clear()

def exit_screen():
    clear()
    print(f"{BLUE}" + "=" * 50 + f"{RESET}")
    type_text("        THANK YOU FOR USING DSA PACKAGE ⚡", YELLOW, 0.03)
    print(f"{BLUE}" + "=" * 50 + f"{RESET}")
    print(f"\n{CYAN}Saving progress...{RESET}")

    bar = ""
    for _ in range(20):
        bar += "█"
        print(f"\r{GREEN}[{bar:<20}]{RESET}", end="")
        time.sleep(0.06)
 
    print(f"\n\n{YELLOW}Goodbye 👋 See you again!{RESET}")
    time.sleep(1.5)


if __name__ == "__main__":
    loading_screen()
    try:
        main_menu()
    finally:
        exit_screen()
        
        