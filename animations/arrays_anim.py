import time
import os

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"


def beep(times=1, delay=0.12, freq_type="normal"):
    sound_map = {
        "normal": "\a",
        "success": "\a",
        "error": "\a",
        "alert": "\a"
    }
    sound = sound_map.get(freq_type, "\a")
    for _ in range(times):
        print(sound, end="", flush=True)
        time.sleep(delay)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec=1.5):
    time.sleep(sec)


def neon_line(width=60):
    print(CYAN + "═" * width + RESET)


def show_array(arr, title="Array", highlight=None):
    neon_line(60)
    print(MAGENTA + BOLD + title.center(60) + RESET)
    neon_line(60)

    boxes = []
    for i, x in enumerate(arr):
        color = GREEN if highlight is not None and i == highlight else YELLOW
        boxes.append(color + BOLD + f"⟪{str(x).center(5)}⟫" + RESET)
    print(" ".join(boxes))

    indexes = " ".join(CYAN + f" {i:^5} " + RESET for i in range(len(arr)))
    print(indexes)
    print(f"\n{CYAN}{BOLD}⚡ Size: {len(arr)}{RESET}")
    neon_line(60)


def insertion_animation():
    arr = [10, 20, 30]
    try:
        value = int(input("\nEnter value to insert: "))
    except ValueError:
        print(RED + "Invalid input!" + RESET)
        pause(1.5)
        return

    for step in range(3):
        clear()
        show_array(arr, "ARRAY INSERTION")
        print(f"\n{BLUE}Moving {value} into array{'.' * (step + 1)}{RESET}")
        print(CYAN + "\n                 ⚡⚡ [ ] ⚡⚡ -->" + RESET)
        pause(0.35)
    arr.append(value)
    beep(1, freq_type="success")
    clear()
    show_array(arr, "AFTER INSERTION", len(arr) - 1)
    print(f"\n{GREEN}{BOLD}>>> Inserted Successfully!{RESET}")
    pause(2)


def deletion_animation():
    arr = [10, 20, 30, 40]
    clear()
    show_array(arr, "ARRAY DELETION")
    try:
        idx = int(input("\nEnter index to delete: "))
    except ValueError:
        print(RED + "Invalid input!" + RESET)
        pause(1.5)
        return

    if idx < 0 or idx >= len(arr):
        print(RED + "Index out of range!" + RESET)
        pause(1.5)
        return

    removed = arr[idx]
    for step in range(3):
        clear()
        show_array(arr, "ARRAY DELETION", idx)
        print(f"\n{YELLOW}Removing {removed}{'.' * (step + 1)}{RESET}")
        print(MAGENTA + "\n<-- ⚡⚡ [ ] ⚡⚡" + RESET)
        pause(0.35)
    arr.pop(idx)
    beep(1, freq_type="alert")
    clear()
    show_array(arr, "AFTER DELETION")
    print(f"\n{GREEN}{BOLD}<<< Removed: {removed}{RESET}")
    pause(2)


def traversal_animation():
    arr = [5, 10, 15, 20]
    clear()
    print("Array Traversal Animation")
    pause()
    for i, val in enumerate(arr):
        clear()
        show_array(arr, "Traversing Array")
        print(f"\nVisiting index {i} -> value {val}")
        pause(1.5)
    print("\nTraversal Completed")
    pause(2)


def searching_animation():
    arr = [3, 7, 9, 12, 15]
    clear()
    show_array(arr, "SEARCH ARRAY")
    try:
        target = int(input("\nEnter value to search: "))
    except ValueError:
        print(RED + "Invalid input!" + RESET)
        pause(1.5)
        return

    for i, val in enumerate(arr):
        clear()
        show_array(arr, "SEARCHING ARRAY", i)
        print(f"\nChecking index {i}: {val}")
        pause(1.2)
        if val == target:
            beep(3, 0.10, "success")
            print(f"\n{GREEN}{BOLD}Found {target} at index {i}{RESET}")
            pause(2)
            return

    print(f"\n{RED}Element not found{RESET}")
    pause(2)


def reverse_animation():
    arr = [1, 2, 3, 4]
    clear()
    print("Array Reverse Animation")
    pause()
    left = 0
    right = len(arr) - 1
    while left < right:
        clear()
        show_array(arr, "Current Array")
        print(f"\nSwapping {arr[left]} and {arr[right]}...")
        pause(2)
        arr[left], arr[right] = arr[right], arr[left]
        beep(1, freq_type="normal")
        left += 1
        right -= 1
    clear()
    print("Final Reversed Array:")
    print(arr)
    pause(2)


def sorting_animation():
    arr = [5, 2, 4, 1]
    clear()
    print("Bubble Sort Animation")
    pause()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            clear()
            show_array(arr, "Bubble Sort")
            print(f"\nComparing {arr[j]} and {arr[j+1]}")
            pause(1.2)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                beep(1, 0.08, "normal")
                clear()
                show_array(arr, "After Swap")
                print("Swapped!")
                pause(1.2)
    print("\nSorted Array:")
    print(arr)
    pause(2)


def array_reverse_animation():
    while True:
        clear()
        print(CYAN + "═" * 40 + RESET)
        print(MAGENTA + BOLD + BLINK + "ARRAY ANIMATIONS".center(40) + RESET)
        print(CYAN + "═" * 40 + RESET)
        beep(1, 0.05, "normal")
        print(GREEN + BOLD + "⚡ 1. Insertion" + RESET)
        print(YELLOW + BOLD + "⚡ 2. Deletion" + RESET)
        print(CYAN + BOLD + "⚡ 3. Traversal" + RESET)
        print(BLUE + BOLD + "⚡ 4. Searching" + RESET)
        print(MAGENTA + BOLD + "⚡ 5. Reverse" + RESET)
        print(WHITE + BOLD + "⚡ 6. Sorting" + RESET)
        print(RED + BOLD + "⚡ 7. Back" + RESET)

        choice = input("Enter choice: ")

        if choice == '1':
            insertion_animation()
        elif choice == '2':
            deletion_animation()
        elif choice == '3':
            traversal_animation()
        elif choice == '4':
            searching_animation()
        elif choice == '5':
            reverse_animation()
        elif choice == '6':
            sorting_animation()
        elif choice == '7':
            break
        else:
            print("Invalid choice")
            beep(2, 0.08, "error")
            pause()