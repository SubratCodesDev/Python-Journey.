word = input("Enter a word: ")

if word.endswith("ing"):
    my_list = list(word)
    print(my_list)
else:
    print("The word does not end with ing")