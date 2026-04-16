import time
import os

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec=1.5):
    time.sleep(sec)


def show_stack(stack, title="STACK", highlight=None):
    clear()
    print(CYAN + "=" * 54 + RESET)
    print((BOLD + title.center(54) + RESET))
    print(CYAN + "=" * 54 + RESET)

    if not stack:
        print(f"\n{RED}{BOLD}        [ EMPTY STACK ]{RESET}\n")
        print(CYAN + "=" * 54 + RESET)
        return

    print()
    for i in range(len(stack) - 1, -1, -1):
        value = stack[i]
        top_text = "  ==> TOP" if i == len(stack) - 1 else ""
        color = GREEN if i == highlight else YELLOW

        print(color + "   --> ┌───────────┐" + RESET)
        print(color + f"       │ {str(value).center(9)} │" + RESET + top_text)
        print(color + "   --> └───────────┘" + RESET)

    print(f"\n{MAGENTA}Size: {len(stack)}{RESET}")
    print(CYAN + "=" * 54 + RESET)


def push_animation(stack):
    try:
        raw = input("\nEnter value to push: ")
        value = int(raw)
    except ValueError:
        print(f"{RED}Invalid number!{RESET}")
        pause(1.5)
        return

    for step in range(3):
        show_stack(stack, "PUSH OPERATION")
        dots = "." * (step + 1)
        print(f"\n{BLUE}Moving {value} into stack{dots}{RESET}")
        print("\n          [ ]")
        pause(0.35)

    stack.append(value)

    show_stack(stack, "AFTER PUSH", len(stack) - 1)
    print(f"\n{GREEN}>>> Push Successful!{RESET}")
    pause(2)


def pop_animation(stack):
    if not stack:
        show_stack(stack, "POP OPERATION")
        print(f"\n{RED}Stack Underflow!{RESET}")
        pause(2)
        return

    removed = stack[-1]
    for step in range(3):
        show_stack(stack, "POP OPERATION", len(stack) - 1)
        dots = "." * (step + 1)
        print(f"\n{YELLOW}Lifting top element {removed}{dots}{RESET}")
        print("\n          [ ^ ]")
        pause(0.35)

    removed = stack.pop()

    show_stack(stack, "AFTER POP")
    print(f"\n{GREEN}<<< Removed: {removed}{RESET}")
    pause(2)


def peek_animation(stack):
    if not stack:
        show_stack(stack, "PEEK OPERATION")
        print(f"\n{RED}Stack is Empty!{RESET}")
        pause(2)
        return

    show_stack(stack, "PEEK OPERATION", len(stack) - 1)
    print(f"\n{GREEN}{BOLD}==> Top Element = {stack[-1]}{RESET}")
    pause(2)


def isempty_animation(stack):
    show_stack(stack, "ISEMPTY CHECK")

    if not stack:
        print(f"\n{GREEN}True → Stack is Empty{RESET}")
    else:
        print(f"\n{YELLOW}False → Stack has elements{RESET}")

    pause(2)


def display_animation(stack):
    show_stack(stack, "DISPLAY STACK")
    pause(2)


def search_animation(stack):
    if not stack:
        show_stack(stack, "SEARCH STACK")
        print(f"\n{RED}Stack is Empty!{RESET}")
        pause(2)
        return

    try:
        target = int(input("\nEnter value to search: "))
    except ValueError:
        print(f"{RED}Invalid number!{RESET}")
        pause(1.5)
        return

    if target in stack:
        idx = stack.index(target)
        show_stack(stack, "SEARCH RESULT", idx)
        print(f"\n{GREEN}Found {target} in stack.{RESET}")
    else:
        show_stack(stack, "SEARCH RESULT")
        print(f"\n{RED}{target} not found.{RESET}")
    pause(2)


def stack_animation():
    stack = []

    while True:
        clear()
        print(CYAN + "=" * 40 + RESET)
        print((BOLD + "STACK ANIMATIONS".center(40) + RESET))
        print(CYAN + "=" * 40 + RESET)

        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Display")
        print("6. Search")
        print("7. Back")

        choice = input("\nEnter choice: ")

        if choice == '1':
            push_animation(stack)

        elif choice == '2':
            pop_animation(stack)

        elif choice == '3':
            peek_animation(stack)

        elif choice == '4':
            isempty_animation(stack)

        elif choice == '5':
            display_animation(stack)

        elif choice == '6':
            search_animation(stack)

        elif choice == '7':
            break

        else:
            print("Invalid choice!")
            pause()