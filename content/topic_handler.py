import time
import tempfile
import subprocess
import os
from services.content_service import get_theory, get_questions, get_code
from services.quiz_service import get_quiz
from utils.quiz_engine import run_quiz
from animations.arrays_anim import array_reverse_animation
from animations.stack_anim import stack_animation
from animations.queue_anim import queue_animation
from animations.linked_list_anim import linked_list_animation
from utils.ui import box_menu

def type_text(text, delay=0.01):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def run_sample_code(code, lang):
    try:
        if lang == "python":
            exec(code, {})
            return

        elif lang == "cpp":
            with tempfile.TemporaryDirectory() as temp_dir:
                cpp_file = os.path.join(temp_dir, "main.cpp")
                exe_file = os.path.join(temp_dir, "main")

                with open(cpp_file, "w") as f:
                    f.write(code)

                compile_result = subprocess.run(
                    ["g++", cpp_file, "-o", exe_file],
                    capture_output=True,
                    text=True
                )

                if compile_result.returncode != 0:
                    print("Compilation Error:\n", compile_result.stderr)
                    return

                run_result = subprocess.run([exe_file], capture_output=True, text=True)
                print(run_result.stdout)
                return

        elif lang == "java":
            with tempfile.TemporaryDirectory() as temp_dir:
                java_file = os.path.join(temp_dir, "Main.java")

                with open(java_file, "w") as f:
                    f.write(code)

                compile_result = subprocess.run(
                    ["javac", java_file],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )

                if compile_result.returncode != 0:
                    print("Compilation Error:\n", compile_result.stderr)
                    return

                run_result = subprocess.run(
                    ["java", "Main"],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )
                print(run_result.stdout)
                return
    except Exception as e:
        print("Run failed:", e)

def handle_topic(topic_name):
    while True:
        title = f"{topic_name.replace('_', ' ').title()} ⚡"
        box_menu(title, [
            ("1", "Theory"),
            ("2", "Code"),
            ("3", "Questions"),
            ("4", "Quiz"),
            ("5", "Animation"),
            ("6", "Back")
        ])

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            type_text(get_theory(topic_name), 0.005)
            input("\nPress Enter to return to menu...")

        elif choice == '2':
            box_menu("SELECT LANGUAGE 💻", [
                ("1", "Python"),
                ("2", "C++"),
                ("3", "Java")
            ])

            lang = input("Choose language: ")

            code = ""
            lang_name = ""
            lang_key = ""

            if lang == '1':
                code = get_code(topic_name, "python")
                lang_name = "Python"
                lang_key = "python"
            elif lang == '2':
                code = get_code(topic_name, "cpp")
                lang_name = "C++"
                lang_key = "cpp"
            elif lang == '3':
                code = get_code(topic_name, "java")
                lang_name = "Java"
                lang_key = "java"
            else:
                input("\nInvalid choice. Press Enter to return...")
                continue

            print(f"\n{lang_name} Code:\n")
            print(code)

            print("\n1. Run Code ▶️")
            print("2. Back")
            run_choice = input("Choose option: ")

            if run_choice == '1':
                print("\nOutput:\n")
                run_sample_code(code, lang_key)

            input("\nPress Enter to return to menu...")

        elif choice == '3':
            questions = get_questions(topic_name)
            print("\n📌 Questions:")
            for q in questions:
                print("-", q)
            input("\nPress Enter to return to menu...")

        elif choice == '4':
            quiz_questions = get_quiz(topic_name)
            run_quiz(quiz_questions, topic_name)

        elif choice == '5':
            if topic_name == "arrays":
                array_reverse_animation()
            elif topic_name == "stack":
                stack_animation()
            elif topic_name == "queue":
                queue_animation()
            elif topic_name == "linked_list":
                linked_list_animation()
            else:
                print("Animation coming soon.")
                input("\nPress Enter to return to menu...")

        elif choice == '6':
            break

        else:
            print("Invalid choice!")
            input("\nPress Enter to continue...")