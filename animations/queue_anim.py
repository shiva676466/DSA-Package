

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


def neon_line(width=70):
    print(CYAN + "═" * width + RESET)


def show_queue(queue, title="QUEUE", front=None, rear=None, highlight=None):
    clear()
    neon_line(70)
    print(MAGENTA + BOLD + title.center(70) + RESET)
    neon_line(70)

    if not queue:
        print(f"\n{RED}{BOLD}           [ EMPTY QUEUE ]{RESET}\n")
        neon_line(70)
        return

    print()
    row = []
    for i, val in enumerate(queue):
        color = GREEN if highlight is not None and i == highlight else YELLOW
        row.append(color + BOLD + f"⟪{str(val).center(5)}⟫" + RESET)
    print(" ".join(row))

    marks = []
    for i in range(len(queue)):
        text = "       "
        if i == front and i == rear:
            text = MAGENTA + " F/R  " + RESET
        elif i == front:
            text = CYAN + " FRONT" + RESET
        elif i == rear:
            text = BLUE + " REAR " + RESET
        marks.append(text)
    print(" ".join(marks))
    print(f"\n{CYAN}{BOLD}⚡ Size: {len(queue)}{RESET}")
    neon_line(70)


def enqueue_animation(queue):
    try:
        value = int(input("\nEnter value to enqueue: "))
    except ValueError:
        print(f"{RED}Invalid number!{RESET}")
        pause(1.5)
        return

    for step in range(3):
        show_queue(queue, "ENQUEUE", front=0 if queue else None, rear=len(queue)-1 if queue else None)
        dots = "." * (step + 1)
        print(f"\n{BLUE}Moving {value} to rear{dots}{RESET}")
        print(CYAN + "\n                    ⚡⚡ [ ] ⚡⚡ -->" + RESET)
        pause(0.35)

    queue.append(value)
    show_queue(queue, "AFTER ENQUEUE", front=0, rear=len(queue)-1, highlight=len(queue)-1)
    print(f"\n{GREEN}>>> Enqueue Successful!{RESET}")
    pause(2)


def dequeue_animation(queue):
    if not queue:
        show_queue(queue, "DEQUEUE")
        print(f"\n{RED}Queue Underflow!{RESET}")
        pause(2)
        return

    removed = queue[0]
    for step in range(3):
        show_queue(queue, "DEQUEUE", front=0, rear=len(queue)-1, highlight=0)
        dots = "." * (step + 1)
        print(f"\n{YELLOW}Removing front element {removed}{dots}{RESET}")
        print(MAGENTA + "\n<-- ⚡⚡ [ ] ⚡⚡" + RESET)
        pause(0.35)

    queue.pop(0)

    if queue:
        show_queue(queue, "AFTER DEQUEUE", front=0, rear=len(queue)-1)
    else:
        show_queue(queue, "AFTER DEQUEUE")
    print(f"\n{GREEN}<<< Removed: {removed}{RESET}")
    pause(2)


def front_animation(queue):
    if not queue:
        show_queue(queue, "FRONT")
        print(f"\n{RED}Queue is Empty!{RESET}")
        pause(2)
        return

    show_queue(queue, "FRONT ELEMENT", front=0, rear=len(queue)-1, highlight=0)
    print(f"\n{GREEN}{BOLD}==> Front = {queue[0]}{RESET}")
    pause(2)


def rear_animation(queue):
    if not queue:
        show_queue(queue, "REAR")
        print(f"\n{RED}Queue is Empty!{RESET}")
        pause(2)
        return

    show_queue(queue, "REAR ELEMENT", front=0, rear=len(queue)-1, highlight=len(queue)-1)
    print(f"\n{GREEN}{BOLD}==> Rear = {queue[-1]}{RESET}")
    pause(2)


def display_animation(queue):
    if queue:
        show_queue(queue, "DISPLAY QUEUE", front=0, rear=len(queue)-1)
    else:
        show_queue(queue, "DISPLAY QUEUE")
    pause(2)


def isempty_animation(queue):
    show_queue(queue, "ISEMPTY CHECK")
    if not queue:
        print(f"\n{GREEN}True → Queue is Empty{RESET}")
    else:
        print(f"\n{YELLOW}False → Queue has elements{RESET}")
    pause(2)


def queue_animation():
    queue = []

    while True:
        clear()
        print(CYAN + "═" * 40 + RESET)
        print(MAGENTA + BOLD + BLINK + "QUEUE ANIMATIONS".center(40) + RESET)
        print(CYAN + "═" * 40 + RESET)
        print(GREEN + "1. Enqueue" + RESET)
        print(YELLOW + "2. Dequeue" + RESET)
        print(CYAN + "3. Front" + RESET)
        print(BLUE + "4. Rear" + RESET)
        print(MAGENTA + "5. Display" + RESET)
        print(WHITE + "6. isEmpty" + RESET)
        print(RED + "7. Back" + RESET)

        choice = input("\nEnter choice: ")

        if choice == '1':
            enqueue_animation(queue)
        elif choice == '2':
            dequeue_animation(queue)
        elif choice == '3':
            front_animation(queue)
        elif choice == '4':
            rear_animation(queue)
        elif choice == '5':
            display_animation(queue)
        elif choice == '6':
            isempty_animation(queue)
        elif choice == '7':
            break
        else:
            print("Invalid choice!")
            pause()