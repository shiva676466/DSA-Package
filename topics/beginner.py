from content.arrays import arrays_content
from content.strings import strings_content
from content.stacks import stacks_content


def beginner_topics():
    while True:
        print("\nBeginner Topics: ")
        print("1. Arrays")
        print("2. Strings")
        print("3. Stack")
        print("4. Queue")
        print("5. LinkedList")
        print("6. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            arrays_content()
        elif choice == '2':
            strings_content()
        elif choice == '3':
            stacks_content()
        elif choice == '4':
            print("Coming Soon.")
        elif choice == '5':
            print("Coming Soon.")
        elif choice == '6':
            print("Exiting....!")
            break
        else:
            print("Invalid Choice")
            