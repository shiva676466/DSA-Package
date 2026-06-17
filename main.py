from menu import main_menu
import time
import os
import sys

RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, colors):
    result = ""
    for i, ch in enumerate(text):
        if ch == " ":
            result += ch
            continue
        r, g, b = colors[i % len(colors)]
        result += f"{rgb(r, g, b)}{ch}"
    return result + RESET

RAINBOW = [
    (255, 0, 0), (255, 127, 0), (255, 255, 0),
    (0, 255, 0), (0, 127, 255), (75, 0, 130), (148, 0, 211)
]

CYAN_GRAD = [
    (0, 200, 255), (0, 220, 240), (0, 240, 220),
    (0, 255, 200), (0, 240, 220), (0, 220, 240)
]

BANNER = [
    "╔══════════════════════════════════════════════════╗",
    "║                                                  ║",
    "║     ██████╗  ███████╗  █████╗                    ║",
    "║     ██╔══██╗ ██╔════╝ ██╔══██╗                   ║",
    "║     ██║  ██║ ███████╗ ███████║                    ║",
    "║     ██║  ██║ ╚════██║ ██╔══██║                    ║",
    "║     ██████╔╝ ███████║ ██║  ██║                    ║",
    "║     ╚═════╝  ╚══════╝ ╚═╝  ╚═╝                   ║",
    "║                                                  ║",
    "║          ⚡  P A C K A G E  ⚡                   ║",
    "║                                                  ║",
    "╚══════════════════════════════════════════════════╝",
]

EXIT_BANNER = [
    "╔══════════════════════════════════════════════════╗",
    "║                                                  ║",
    "║        ✦  T H A N K   Y O U  ✦                  ║",
    "║                                                  ║",
    "║      For using DSA Package                       ║",
    "║      See you next time! 👋                       ║",
    "║                                                  ║",
    "╚══════════════════════════════════════════════════╝",
]

SPINNER = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

def fade_in_banner(banner, colors, delay=0.06):
    for i, line in enumerate(banner):
        colored = gradient_text(line, colors)
        print(colored)
        time.sleep(delay)

def spinner_progress(label, duration=2.0, bar_width=30):
    steps = bar_width
    interval = duration / steps
    for i in range(steps + 1):
        spin = SPINNER[i % len(SPINNER)]
        filled = "━" * i
        empty = " " * (bar_width - i)
        pct = int(i / steps * 100)
        r = int(255 - (i / steps) * 255)
        g = int((i / steps) * 255)
        bar_color = rgb(r, g, 100)
        print(f"\r  {rgb(0,200,255)}{spin}{RESET} {label} {bar_color}▐{filled}{empty}▌{RESET} {pct}%", end="", flush=True)
        time.sleep(interval)
    print(f"\r  {rgb(0,255,100)}✔{RESET} {label} {rgb(0,255,100)}▐{'━' * bar_width}▌{RESET} 100%")

def loading_screen():
    clear()
    print()
    fade_in_banner(BANNER, RAINBOW)
    print()
    spinner_progress("Initializing", duration=1.8)
    spinner_progress("Loading modules", duration=1.2)
    print(f"\n  {rgb(255,255,0)}{BOLD}⚡ Ready to Launch 🚀{RESET}\n")
    time.sleep(0.8)
    clear()

def exit_screen():
    clear()
    print()
    fade_in_banner(EXIT_BANNER, CYAN_GRAD, delay=0.08)
    print()
    spinner_progress("Saving progress", duration=1.5)
    print(f"\n  {rgb(148,0,211)}{BOLD}✦ Goodbye! ✦{RESET}\n")
    time.sleep(1.2)


if __name__ == "__main__":
    loading_screen()
    try:
        main_menu()
    finally:
        exit_screen()
        
        