import json

def stacks_content():
    while True:
        print("\n========== Stack ==========")
        print("1. Theory")
        print("2. Code")
        print("3. Questions")
        print("4. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("")
        elif choice == '2':
            print("\n--- Stack Code Examples ---")