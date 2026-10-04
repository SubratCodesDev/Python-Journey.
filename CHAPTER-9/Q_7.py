file = open("do.txt", "w")
file.write("Gettinf tired try to rest not to give up.")
print(file)
file.close()

file = open("do.txt", "r")
content = file.read()
print(content)
file.close()