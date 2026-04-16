from utils.file_handler import load_json

def arrays_content():
    while True:
        print("\n--- Arrays ---")
        print("1. Theory")
        print("2. Code")
        print("3. Questions")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            data = load_json("theory.json")
            print(data["arrays"])

        elif choice == '2':
            data = load_json("code.json")

            print("1. Python\n2. C++\n3. Java")
            lang = input("Choose: ")

            if lang == '1':
                print(data["arrays"]["python"])
            elif lang == '2':
                print(data["arrays"]["cpp"])
            elif lang == '3':
                print(data["arrays"]["java"])

        elif choice == '3':
            data = load_json("questions.json")
            for q in data["arrays"]:
                print("-", q)

        elif choice == '4':
            break