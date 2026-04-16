from topics.beginner import beginner_topics
from topics.intermediate import intermediate_topics
from topics.advanced import advanced_topics


def select_level():
    print("\nSelect Your Level: ")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        beginner_topics()
    elif choice == '2':
        intermediate_topics()
    elif choice == '3':
        advanced_topics()
    else:
        print("Invalid choice!")
