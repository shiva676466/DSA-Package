from content.arrays import arrays_content


def beginner_topics():
    while True:
        print("\nBeginner Topics: ")
        print("1. Arrays")
        print("2. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            arrays_content()
        elif choice == '2':
            print("Exiting....!")
            break
        else:
            print("Invalid Choice")