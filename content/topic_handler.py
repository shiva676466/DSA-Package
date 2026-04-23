import time
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
            import os
            box_menu("SELECT LANGUAGE 💻", [
                ("1", "Python"),
                ("2", "C++"),
                ("3", "Java")
            ])

            lang = input("Choose language: ")

            code = None
            lang_key = None
            if lang == '1':
                code = get_code(topic_name, "python")
                lang_key = "python"
            elif lang == '2':
                code = get_code(topic_name, "cpp")
                lang_key = "cpp"
            elif lang == '3':
                code = get_code(topic_name, "java")
                lang_key = "java"

            if code is not None:
                print(code)
                print("\n1. Run Code ▶️")
                print("2. Copy Code 📋")
                print("3. Back")
                run_choice = input("Choose option: ")

                if run_choice == '1':
                    print("\nOutput:\n")
                    run_sample_code(code, lang_key)

                elif run_choice == '2':
                    os.makedirs("exports", exist_ok=True)

                    ext_map = {
                        "python": "py",
                        "cpp": "cpp",
                        "java": "java"
                    }

                    file_name = f"{topic_name}.{ext_map[lang_key]}"
                    file_path = os.path.join("exports", file_name)

                    with open(file_path, "w") as f:
                        f.write(code)

                    print(f"\nCode copied to file: {file_path} 📋")

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