print('''-----+++|WELCOME TO FILE MANAGER X|+++-----
            1. READ THE FILE
            2. WRITE IN THE FILE
            3. APPEND TO THE FILE
            4. EXIT''')
while True:
    n = int(input("Enter the serial no of the command you want to execute: "))
    if n == 1:
        a = open("file manager", "r")
        aa = a.read()
        print(aa)
        a.close()
    elif n == 2:
        nn = input("Enter what you want to write in the file: ")
        a = open("file manager", "w")
        aa = a.write(nn + "\n")
        a.close()
    elif n == 3:
        nnn = input("Enter what you want to append in the file: ")
        a = open("file manager", "a")
        aa = a.write(nnn + "\n")
        a.close()
    elif n == 4:
        print("FILE MANAGER CLOSED")
        break
    else:
        print("INVALID REQUEST, TRY AGAIN.....")