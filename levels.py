from topics.beginner import beginner_topics
from topics.intermediate import intermediate_topics
from topics.advanced import advanced_topics
from utils.ui import box_menu


def select_level():
    box_menu("DSA PACKAGE ⚡", [
        ("1", "Beginner"),
        ("2", "Intermediate"),
        ("3", "Advanced"),
        ("4", "Exit")
    ])

    choice = input("Enter your choice: ")
    
    if choice == '1':
        beginner_topics()
    elif choice == '2':
        intermediate_topics()
    elif choice == '3':
        advanced_topics()
    elif choice == '4':
        return
    else:
        print("Invalid choice!")
