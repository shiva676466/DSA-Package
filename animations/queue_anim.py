

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


def show_queue(queue, title="QUEUE", front=None, rear=None, highlight=None):
    clear()
    print("=" * 70)
    print(title.center(70))
    print("=" * 70)

    if not queue:
        print(f"{RED}[ EMPTY QUEUE ]{RESET}")
        print("=" * 70)
        return

    row = []
    for i, val in enumerate(queue):
        if highlight is not None and i == highlight:
            row.append(f"{GREEN}[{val}]{RESET}")
        else:
            row.append(f"[{val}]")
    print(" ".join(row))

    marks = []
    for i in range(len(queue)):
        text = "   "
        if i == front and i == rear:
            text = f"{YELLOW}F/R{RESET}"
        elif i == front:
            text = f"{YELLOW} F {RESET}"
        elif i == rear:
            text = f"{BLUE} R {RESET}"
        marks.append(text)
    print(" ".join(marks))
    print("=" * 70)


def enqueue_animation(queue):
    value = len(queue) * 10 + 10
    show_queue(queue, "ENQUEUE")
    print(f"\nAdding {value} to rear...")
    pause()
    queue.append(value)
    show_queue(queue, "AFTER ENQUEUE", front=0, rear=len(queue)-1, highlight=len(queue)-1)
    pause(2)


def dequeue_animation(queue):
    if not queue:
        show_queue(queue, "DEQUEUE")
        print(f"\n{RED}Queue Underflow!{RESET}")
        pause(2)
        return

    show_queue(queue, "DEQUEUE", front=0, rear=len(queue)-1, highlight=0)
    print(f"\nRemoving front element {queue[0]}...")
    pause(2)
    queue.pop(0)

    if queue:
        show_queue(queue, "AFTER DEQUEUE", front=0, rear=len(queue)-1)
    else:
        show_queue(queue, "AFTER DEQUEUE")
    pause(2)


def front_animation(queue):
    if not queue:
        show_queue(queue, "FRONT")
        print(f"\n{RED}Queue is Empty!{RESET}")
        pause(2)
        return

    show_queue(queue, "FRONT ELEMENT", front=0, rear=len(queue)-1, highlight=0)
    print(f"\nFront = {GREEN}{queue[0]}{RESET}")
    pause(2)


def rear_animation(queue):
    if not queue:
        show_queue(queue, "REAR")
        print(f"\n{RED}Queue is Empty!{RESET}")
        pause(2)
        return

    show_queue(queue, "REAR ELEMENT", front=0, rear=len(queue)-1, highlight=len(queue)-1)
    print(f"\nRear = {GREEN}{queue[-1]}{RESET}")
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
        print("=" * 40)
        print("QUEUE ANIMATIONS".center(40))
        print("=" * 40)
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Rear")
        print("5. Display")
        print("6. isEmpty")
        print("7. Back")

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