

from content.trees import trees_content
from content.sorting import sorting_content
from content.searching import searching_content
from content.recursion import recursion_content


def intermediate_topics():
    while True:
        print("\nIntermediate Topics:")
        print("1. Trees")
        print("2. Sorting")
        print("3. Searching")
        print("4. Recursion")
        print("5. Back")

        choice = input("Enter choice: ")

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