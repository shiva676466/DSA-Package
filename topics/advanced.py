from content.graphs import graphs_content
from content.heap import heap_content
from content.dynamic_programming import dynamic_programming_content
from content.trie import trie_content


def advanced_topics():
    while True:
        print("\nAdvanced Topics:")
        print("1. Graphs")
        print("2. Heap")
        print("3. Dynamic Programming")
        print("4. Trie")
        print("5. Back")

        choice = input("Enter choice: ")

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
