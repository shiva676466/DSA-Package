from content.graphs import graphs_content
from content.heap import heap_content
from content.dynamic_programming import dynamic_programming_content
from content.trie import trie_content
from utils.ui import box_menu


def advanced_topics():
    while True:
        box_menu("ADVANCED TOPICS 📕", [
            ("1", "Graphs"),
            ("2", "Heap"),
            ("3", "Dynamic Programming"),
            ("4", "Trie"),
            ("5", "Back")
        ])

        choice = input("Enter your choice: ")

        if choice == '1':
            graphs_content()
        elif choice == '2':
            heap_content()
        elif choice == '3':
            dynamic_programming_content()
        elif choice == '4':
            trie_content()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
