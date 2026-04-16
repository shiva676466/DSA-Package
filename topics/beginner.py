from content.arrays import arrays_content
from content.strings import strings_content
from content.stacks import stacks_content
from content.queue import queue_content
from content.linked_list import linked_list_content
from utils.ui import box_menu


def beginner_topics():
    while True:
        box_menu("BEGINNER TOPICS 📘", [
            ("1", "Arrays"),
            ("2", "Strings"),
            ("3", "Stack"),
            ("4", "Queue"),
            ("5", "Linked List"),
            ("6", "Back")
        ])
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            arrays_content()
        elif choice == '2':
            strings_content()
        elif choice == '3':
            stacks_content()
        elif choice == '4':
            queue_content()
        elif choice == '5':
            linked_list_content()
        elif choice == '6':
            print("Returning to previous menu...")
            break
        else:
            print("Invalid choice!")