from topics.beginner import beginner_topics


def select_level():
    print("\nSelect Your Level: ")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        beginner_topics()
    else:
        print("Topics coming soon please wait.....")


        # /added sone changes