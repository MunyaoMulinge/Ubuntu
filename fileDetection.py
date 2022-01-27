import os
path = "folder"
if os.path.exists(path):
    print("There is proof it exists.")
    if os.path.isfile(path):
        print("This is a file.")
    elif os.path.isdir(path):
        print("This is a folder.")
else:
    print("No proof the file exists.")
