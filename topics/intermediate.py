from content.trees import trees_content
from content.sorting import sorting_content
from content.searching import searching_content
from content.recursion import recursion_content
from utils.ui import box_menu


def intermediate_topics():
    while True:
        box_menu("INTERMEDIATE TOPICS 📗", [
            ("1", "Trees"),
            ("2", "Sorting"),
            ("3", "Searching"),
            ("4", "Recursion"),
            ("5", "Back")
        ])

        choice = input("Enter your choice: ")

        if choice == '1':
            trees_content()
        elif choice == '2':
            sorting_content()
        elif choice == '3':
            searching_content()
        elif choice == '4':
            recursion_content()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")