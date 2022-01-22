name = input("Enter student's name:\n")
grade = int(input("Enter student's grade\n"))

if grade >= 90:
    print("Grade A+")
    print(f"Congrats {name}")

elif grade >= 80:
    print("Grade A")
    print(f"Aim Higher {name}")

elif grade >= 70:
    print("Grade B+")
    print(f"More like it {name}")

elif grade >= 65:
    print("Grade B-")
    print(f"Keep trying {name}")

elif grade >= 50:
    print("Grade C+")
    print(f"Can do better {name}")

elif grade >= 40:
    print("Grade C")
    print(f"Is this some kind of joke to you? {name}")

else:
    print("Failed Successfully!\nPull up your socks son.")
