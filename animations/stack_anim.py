import time
import os

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BOLD = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec=1.5):
    time.sleep(sec)


def neon_line(width=54):
    print(CYAN + "═" * width + RESET)


def show_stack(stack, title="STACK", highlight=None):
    clear()
    neon_line(54)
    print(MAGENTA + BOLD + title.center(54) + RESET)
    neon_line(54)

    if not stack:
        print(f"\n{RED}{BOLD}        [ EMPTY STACK ]{RESET}\n")
        neon_line(54)
        return

    print()
    for i in range(len(stack) - 1, -1, -1):
        value = stack[i]
        top_text = "  ==> TOP" if i == len(stack) - 1 else ""
        color = GREEN if i == highlight else YELLOW

        print(color + BOLD + "   ⚡ ┌───────────┐" + RESET)
        print(color + BOLD + f"   ⚡ │ {str(value).center(9)} │" + RESET + top_text)
        print(color + BOLD + "   ⚡ └───────────┘" + RESET)

    print(f"\n{CYAN}{BOLD}⚡ Size: {len(stack)}{RESET}")
    neon_line(54)


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
        print(CYAN + "\n          ⚡⚡ [ ] ⚡⚡" + RESET)
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
        print(MAGENTA + "\n          ⚡⚡ [ ^ ] ⚡⚡" + RESET)
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
        print(CYAN + "═" * 40 + RESET)
        print(MAGENTA + BOLD + BLINK + "STACK ANIMATIONS".center(40) + RESET)
        print(CYAN + "═" * 40 + RESET)

        print(GREEN + BOLD + "⚡ 1. Push" + RESET)
        print(YELLOW + BOLD + "⚡ 2. Pop" + RESET)
        print(CYAN + BOLD + "⚡ 3. Peek" + RESET)
        print(BLUE + BOLD + "⚡ 4. isEmpty" + RESET)
        print(MAGENTA + BOLD + "⚡ 5. Display" + RESET)
        print(WHITE + BOLD + "⚡ 6. Search" + RESET)
        print(RED + BOLD + "⚡ 7. Back" + RESET)

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