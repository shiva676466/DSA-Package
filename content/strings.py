import json
def strings_content():
    while True:
        print("\n========== Strings ==========")
        print("1. Theory")
        print("2. Code")
        print("3. Questions")
        print("4. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("String is a collection of characters that stored in a contious memory locations.")
        elif choice == '2':
            print("\n--- String Code Examples ---")
            
            # Reverse a string
            s = "hello"
            print("Original:", s)
            print("Reversed:", s[::-1])
            
            # Check palindrome
            s2 = "madam"
            if s2 == s2[::-1]:
                print(f"{s2} is a palindrome")
            else:
                print(f"{s2} is not a palindrome")
            
            # Count vowels
            s3 = "programming"
            vowels = "aeiou"
            count = sum(1 for char in s3 if char in vowels)
            print("Vowel count in", s3, ":", count)
            
            # Convert to uppercase
            print("Uppercase:", s3.upper())
            
            # String concatenation
            a = "Data"
            b = "Structures"
            print("Concatenated:", a + " " + b)
            
            # Find length of string
            s4 = "algorithm"
            print("Length of", s4, ":", len(s4))

            # Check substring
            sub = "algo"
            print(f"Is '{sub}' in '{s4}'?", sub in s4)

            # Replace characters
            print("Replace 'a' with 'x':", s4.replace('a', 'x'))

            # Split string
            sentence = "data structures and algorithms"
            words = sentence.split()
            print("Split words:", words)

            # Join strings
            joined = "-".join(words)
            print("Joined with hyphen:", joined)

            # Remove spaces
            spaced = "  hello world  "
            print("Trimmed string:", spaced.strip())

            # Count occurrences of a character
            print("Count of 'a' in", s4, ":", s4.count('a'))

            # Find index of character
            print("Index of 'r' in", s4, ":", s4.find('r'))
        elif choice == '3':
            print("🚀Questions are coming soon...")
        elif choice == '4':
            print("Exiting...!")
            break
        else:
            print("Invalid Choice")
            
            
            # sdfgh