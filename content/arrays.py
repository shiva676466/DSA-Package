import json

# load data function
def load_data(filename):
    with open(f"data/{filename}", "r") as file:
        return json.load(file)
    
def arrays_content():
    while True:
        print("\n========== Arrays ==========")
        print("1. Theory")
        print("2. Code")
        print("3. Questions")
        print("4. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = load_data("theory.json")       
            print("\n" + data["arrays"])
            
        elif choice == '2':
            print("\nPython Example: ")
            print("arr = [1,2,3,4]")
            print("print(arr)")
            
        elif choice == '3':
            show_questions()
            
        elif choice == '4':
            print("Exiting....")
            break
        else:
            print("Invalid Choice")
            
            
def show_questions():
    try:
        with open("data/questions.json", "r") as file:
            data = json.load(file)
            
        questions = data.get("arrays", [])
        
        print("\n===== Arrays =====")
        
        for i, q in enumerate(questions, 1):
            print(f"{i}. {q}")
            
    except Exception as e:
        print("Error loading questions: ", e)
            
