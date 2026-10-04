with open("files.3.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

with open("files.3.txt", "r") as file:
    content = file.read()
    print(content)