import time
import os

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec=1.5):
    time.sleep(sec)


def show_stack(stack, title="STACK", highlight=None):
    clear()
    print("=" * 50)
    print(title.center(50))
    print("=" * 50)

    if not stack:
        print(f"{RED}   [ EMPTY ]{RESET}")
        print("=" * 50)
        return

    for i in range(len(stack) - 1, -1, -1):
        value = stack[i]

        if i == highlight:
            print(f"{GREEN}   ┌───────┐{RESET}")
            print(f"{GREEN}   │ {str(value).center(5)} │   ← TOP{RESET}")
            print(f"{GREEN}   └───────┘{RESET}")
        else:
            top_text = " ← TOP" if i == len(stack) - 1 else ""
            print("   ┌───────┐")
            print(f"   │ {str(value).center(5)} │{top_text}")
            print("   └───────┘")

    print("=" * 50)


def push_animation(stack):
    value = len(stack) * 10 + 10

    show_stack(stack, "PUSH OPERATION")
    print(f"\nPushing {value}...")
    pause()

    stack.append(value)

    show_stack(stack, "AFTER PUSH", len(stack) - 1)
    pause(2)


def pop_animation(stack):
    if not stack:
        show_stack(stack, "POP OPERATION")
        print(f"\n{RED}Stack Underflow!{RESET}")
        pause(2)
        return

    show_stack(stack, "POP OPERATION", len(stack) - 1)
    print(f"\nRemoving top element {stack[-1]}...")
    pause(2)

    stack.pop()

    show_stack(stack, "AFTER POP")
    pause(2)


def peek_animation(stack):
    if not stack:
        show_stack(stack, "PEEK OPERATION")
        print(f"\n{RED}Stack is Empty!{RESET}")
        pause(2)
        return

    show_stack(stack, "PEEK OPERATION", len(stack) - 1)
    print(f"\nTop Element = {GREEN}{stack[-1]}{RESET}")
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


def stack_animation():
    stack = []

    while True:
        clear()
        print("=" * 40)
        print("STACK ANIMATIONS".center(40))
        print("=" * 40)

        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Display")
        print("6. Back")

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
            break

        else:
            print("Invalid choice!")
            pause()