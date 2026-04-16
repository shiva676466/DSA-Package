from services.content_service import get_theory, get_questions, get_code
from services.quiz_service import get_quiz
from utils.quiz_engine import run_quiz
from animations.arrays_anim import array_reverse_animation
from animations.stack_anim import stack_animation

def handle_topic(topic_name):
    while True:
        print(f"\n--- {topic_name.capitalize()} ---")
        print("1. Theory")
        print("2. Code")
        print("3. Questions")
        print("4. Quiz")
        print("5. Animation")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            print("\n" + get_theory(topic_name))

        elif choice == '2':
            print("\nSelect Language:")
            print("1. Python")
            print("2. C++")
            print("3. Java")

            lang = input("Choose: ")

            if lang == '1':
                print(get_code(topic_name, "python"))
            elif lang == '2':
                print(get_code(topic_name, "cpp"))
            elif lang == '3':
                print(get_code(topic_name, "java"))

        elif choice == '3':
            questions = get_questions(topic_name)
            print("\nQuestions:")
            for q in questions:
                print("-", q)

        elif choice == '4':
            quiz_questions = get_quiz(topic_name)
            run_quiz(quiz_questions)

        elif choice == '5':
            if topic_name == "arrays":
                array_reverse_animation()
            elif topic_name == "stack":
                stack_animation()
            else:
                print("Animation coming soon.")

        elif choice == '6':
            break

        else:
            print("Invalid choice!")