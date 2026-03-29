from levels import select_level

def main_menu():
    while True:
        print("\n=============== Learn DSA ==================")
        print("1.Start")
        print("2.Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            select_level()
        elif choice == '2':
            print("Exiting....!")
            break
        else:
            print("Invalid Choice, please enter '1' or '2'")
