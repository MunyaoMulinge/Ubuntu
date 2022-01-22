name = input("Enter student's name:\n")
grade = int(input("Enter student's grade\n"))

if 90 <= grade <= 100:
    print("Grade A+")
    print(f"Congrats {name}")

elif 80 <= grade <= 89:
    print("Grade A")
    print(f"Aim Higher {name}")

elif 70 <= grade <= 79:
    print("Grade B+")
    print(f"More like it {name}")

elif 60 <= grade <= 69:
    print("Grade B-")
    print(f"Keep trying {name}")

elif 50 <= grade <= 59:
    print("Grade C+")
    print(f"Can do better {name}")

elif 40 <= grade <= 49:
    print("Grade C")
    print(f"Is this some kind of joke to you? {name}")
    
elif grade >= 100:
    print("Grade A alpha")
    print(f"Sasawa chopi? {name}")


else:
    print("Failed Successfully!\nPull up your socks son.")
