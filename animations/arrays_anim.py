import time
import os

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
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


def show_array(arr, title="Array"):
    print("=" * 50)
    print(title.center(50))
    print("=" * 50)
    boxes = " ".join(f"[{x}]" for x in arr)
    indexes = " ".join(f" {i} " for i in range(len(arr)))
    print(boxes)
    print(indexes)
    print("=" * 50)


def insertion_animation():
    arr = [10, 20, 30]
    clear()
    print("Array Insertion Animation")
    pause()
    show_array(arr, "Initial Array:")
    pause()
    print("\nInserting 40 at end...")
    pause()
    arr.append(40)
    beep(1, freq_type="success")
    clear()
    show_array(arr, "Updated Array:")
    pause(2)


def deletion_animation():
    arr = [10, 20, 30, 40]
    clear()
    print("Array Deletion Animation")
    pause()
    show_array(arr, "Initial Array:")
    pause()
    print("\nDeleting element 20...")
    pause()
    idx = arr.index(20)
    arr.pop(idx)
    beep(1, freq_type="alert")
    clear()
    show_array(arr, "Updated Array:")
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
    target = 12
    clear()
    print("Linear Search Animation")
    pause()
    for i, val in enumerate(arr):
        clear()
        show_array(arr, "Searching Array")
        print(f"\nChecking index {i}: {val}")
        pause(1.5)
        if val == target:
            beep(3, 0.10, "success")
            print(f"Found {target} at index {i}")
            pause(2)
            return
    print("Element not found")
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
        print("ARRAY ANIMATIONS")
        beep(1, 0.05, "normal")
        print("=" * 30)
        print("1. Insertion")
        print("2. Deletion")
        print("3. Traversal")
        print("4. Searching")
        print("5. Reverse")
        print("6. Sorting")
        print("7. Back")

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