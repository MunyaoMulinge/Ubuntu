import os

location = "doc.txt"
if os.path.exists(location):
    print("Path exists")
else:
    print("Unable to locate path")
