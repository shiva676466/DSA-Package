import time
import os

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def bg_rgb(r, g, b):
    return f"\033[48;2;{r};{g};{b}m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(sec=1.5):
    time.sleep(sec)

SPINNER = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

RAINBOW = [
    (255, 0, 0), (255, 127, 0), (255, 255, 0),
    (0, 255, 0), (0, 127, 255), (75, 0, 130), (148, 0, 211)
]

def gradient_text(text, colors):
    result = ""
    ci = 0
    for ch in text:
        if ch == " ":
            result += ch
        else:
            r, g, b = colors[ci % len(colors)]
            result += f"{rgb(r, g, b)}{ch}"
            ci += 1
    return result + RESET

def neon_border(width=60, top=True):
    ch = "╔" if top else "╚"
    end = "╗" if top else "╝"
    print(rgb(0, 200, 255) + ch + "═" * (width - 2) + end + RESET)

def neon_title(title, width=60):
    neon_border(width, top=True)
    colored = gradient_text(title, RAINBOW)
    pad = (width - 2 - len(title)) // 2
    print(rgb(0, 200, 255) + "║" + " " * pad + colored + " " * (width - 2 - pad - len(title)) + rgb(0, 200, 255) + "║" + RESET)
    neon_border(width, top=False)

def show_array(arr, title="Array", highlight=None, highlight_color=None, secondary=None):
    if highlight_color is None:
        highlight_color = (0, 255, 100)
    clear()
    print()
    neon_title(f"⚡ {title} ⚡")
    print()

    boxes = []
    for i, x in enumerate(arr):
        val = str(x).center(5)
        if highlight is not None and i == highlight:
            r, g, b = highlight_color
            boxes.append(f" {bg_rgb(r, g, b)}{rgb(0,0,0)}{BOLD} {val} {RESET} ")
        elif secondary is not None and i == secondary:
            boxes.append(f" {bg_rgb(255, 165, 0)}{rgb(0,0,0)}{BOLD} {val} {RESET} ")
        else:
            boxes.append(f" {rgb(200,200,255)}⟪{rgb(255,255,0)}{BOLD}{val}{RESET}{rgb(200,200,255)}⟫{RESET} ")
    print("  " + "".join(boxes))

    idx_line = ""
    for i in range(len(arr)):
        if highlight is not None and i == highlight:
            idx_line += f" {rgb(*highlight_color)}{BOLD}  {i:^3}  {RESET} "
        else:
            idx_line += f" {rgb(100,100,180)}  {i:^3}  {RESET} "
    print("  " + idx_line)

    print(f"\n  {rgb(0,200,255)}Size: {len(arr)}{RESET}")
    print()

def spinner_step(msg, step, total, frame):
    spin = SPINNER[frame % len(SPINNER)]
    pct = int((step + 1) / total * 100)
    r = int(255 - (step / max(total - 1, 1)) * 255)
    g = int((step / max(total - 1, 1)) * 255)
    bar_w = 20
    filled = int((step + 1) / total * bar_w)
    bar = "━" * filled + " " * (bar_w - filled)
    print(f"\r  {rgb(0,200,255)}{spin}{RESET} {msg} {rgb(r, g, 100)}▐{bar}▌{RESET} {pct}%", end="", flush=True)

def operation_complete(msg):
    print(f"\n  {rgb(0,255,100)}✔ {BOLD}{msg}{RESET}\n")

def arrow_animation(direction="right", label="", frames=6, delay=0.12):
    arrows_r = ["  ●", "  ●━━", "  ●━━━━", "  ●━━━━━━", "  ●━━━━━━━━▶"]
    arrows_l = ["          ●", "      ━━●", "    ━━━━●", "  ━━━━━━●", "◀━━━━━━━━●"]
    arrows = arrows_r if direction == "right" else arrows_l
    for i, a in enumerate(arrows[:frames]):
        r = int((i / max(len(arrows) - 1, 1)) * 255)
        g = 255 - r
        print(f"\r  {rgb(r if direction == 'left' else 0, g, 255)}{a}{RESET}  {rgb(255,255,0)}{label}{RESET}", end="", flush=True)
        time.sleep(delay)
    print()


def insertion_animation():
    arr = [10, 20, 30]
    show_array(arr, "INSERTION")
    try:
        value = int(input(f"  {rgb(0,200,255)}Enter value to insert: {RESET}"))
    except ValueError:
        print(f"  {rgb(255,0,0)}Invalid input!{RESET}")
        pause(1)
        return

    steps = 5
    for i in range(steps):
        show_array(arr, "INSERTING...")
        spinner_step(f"Moving {value} into array", i, steps, i)
        time.sleep(0.3)

    print()
    arrow_animation("right", f"Placing {value}")
    arr.append(value)
    show_array(arr, "AFTER INSERTION", len(arr) - 1)
    operation_complete(f"Inserted {value} successfully!")
    pause(2)


def deletion_animation():
    arr = [10, 20, 30, 40]
    show_array(arr, "DELETION")
    try:
        idx = int(input(f"  {rgb(0,200,255)}Enter index to delete: {RESET}"))
    except ValueError:
        print(f"  {rgb(255,0,0)}Invalid input!{RESET}")
        pause(1)
        return

    if idx < 0 or idx >= len(arr):
        print(f"  {rgb(255,0,0)}Index out of range!{RESET}")
        pause(1)
        return

    removed = arr[idx]
    steps = 5
    for i in range(steps):
        show_array(arr, "DELETING...", idx, (255, 80, 80))
        spinner_step(f"Removing {removed}", i, steps, i)
        time.sleep(0.3)

    print()
    arrow_animation("left", f"Extracting {removed}")
    arr.pop(idx)
    show_array(arr, "AFTER DELETION")
    operation_complete(f"Removed {removed} from index {idx}")
    pause(2)


def traversal_animation():
    arr = [5, 10, 15, 20]
    for i, val in enumerate(arr):
        show_array(arr, "TRAVERSAL", i, (0, 180, 255))
        pct = int((i + 1) / len(arr) * 100)
        bar_w = 20
        filled = int((i + 1) / len(arr) * bar_w)
        bar = "━" * filled + " " * (bar_w - filled)
        print(f"  {rgb(0,200,255)}Visiting:{RESET} index {rgb(255,255,0)}{i}{RESET} → value {rgb(0,255,100)}{BOLD}{val}{RESET}")
        print(f"  {rgb(0,180,255)}Progress ▐{bar}▌ {pct}%{RESET}")
        pause(1.2)

    show_array(arr, "TRAVERSAL COMPLETE")
    operation_complete("All elements visited!")
    pause(2)


def searching_animation():
    arr = [3, 7, 9, 12, 15]
    show_array(arr, "SEARCH")
    try:
        target = int(input(f"  {rgb(0,200,255)}Enter value to search: {RESET}"))
    except ValueError:
        print(f"  {rgb(255,0,0)}Invalid input!{RESET}")
        pause(1)
        return

    for i, val in enumerate(arr):
        color = (255, 200, 0) if val != target else (0, 255, 100)
        show_array(arr, "SEARCHING...", i, color)
        spinner_step(f"Checking index {i}: {val}", i, len(arr), i)
        time.sleep(0.8)
        print()

        if val == target:
            show_array(arr, "FOUND!", i, (0, 255, 100))
            operation_complete(f"Found {target} at index {i}")
            pause(2)
            return

    show_array(arr, "NOT FOUND")
    print(f"  {rgb(255,80,80)}{BOLD}✗ Element {target} not found{RESET}\n")
    pause(2)


def reverse_animation():
    arr = [1, 2, 3, 4]
    left, right = 0, len(arr) - 1

    while left < right:
        show_array(arr, "REVERSING", left, (0, 200, 255), right)
        print(f"  {rgb(255,165,0)}Swapping arr[{left}]={arr[left]} ↔ arr[{right}]={arr[right]}{RESET}")
        pause(0.5)

        steps = 4
        for s in range(steps):
            show_array(arr, "REVERSING", left, (0, 200, 255), right)
            spinner_step(f"Swapping {arr[left]} ↔ {arr[right]}", s, steps, s)
            time.sleep(0.25)
        print()

        arr[left], arr[right] = arr[right], arr[left]
        show_array(arr, "SWAPPED!", left, (0, 255, 100), right)
        pause(0.8)
        left += 1
        right -= 1

    show_array(arr, "REVERSED")
    operation_complete("Array reversed!")
    pause(2)


def sorting_animation():
    arr = [5, 2, 4, 1]
    n = len(arr)
    total_ops = sum(n - i - 1 for i in range(n))
    op = 0

    for i in range(n):
        for j in range(n - i - 1):
            show_array(arr, "BUBBLE SORT", j, (255, 200, 0), j + 1)
            print(f"  {rgb(255,200,0)}Comparing: {arr[j]} vs {arr[j+1]}{RESET}")
            spinner_step("Sorting", op, total_ops, op)
            time.sleep(0.6)
            print()

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                show_array(arr, "SWAPPED!", j, (0, 255, 100), j + 1)
                print(f"  {rgb(0,255,100)}↕ Swapped!{RESET}")
                pause(0.6)
            op += 1

    show_array(arr, "SORTED")
    operation_complete("Array sorted!")
    pause(2)


def array_reverse_animation():
    menu_items = [
        ("1", "Insertion", (255, 80, 80)),
        ("2", "Deletion", (255, 165, 0)),
        ("3", "Traversal", (0, 200, 255)),
        ("4", "Searching", (0, 255, 100)),
        ("5", "Reverse", (148, 0, 211)),
        ("6", "Sorting", (255, 255, 0)),
        ("7", "Back", (128, 128, 128)),
    ]

    while True:
        clear()
        print()
        neon_title("⚡ ARRAY ANIMATIONS ⚡")
        print()
        for key, label, (r, g, b) in menu_items:
            icon = "◀" if key == "7" else "▸"
            print(f"  {rgb(r, g, b)}{BOLD}{icon} {key}. {label}{RESET}")
        print()

        choice = input(f"  {rgb(0,200,255)}Enter choice: {RESET}")

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
            print(f"  {rgb(255,80,80)}Invalid choice{RESET}")
            pause(1)
