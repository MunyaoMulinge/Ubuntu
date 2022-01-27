try:
    with open("file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Can't find this file son.")