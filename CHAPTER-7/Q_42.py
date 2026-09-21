while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Product")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor division")
    print("7. Power")
    a=input("Enter your desired operation:")
    if a=="exit":
       print("calculator closed")
       break 
    b=int(input("Enter your first number:"))
    c=int(input("Enter your second number:"))

    if a=="add":
        print("sum = ",b+c)
    elif a=="subtract":
        print("subtraction =",b-c)
    elif a=="product":
        print("product =",b*c)
    elif a=="divide":
        print("divison=",b/c)
    elif a=="modulus":
        print("modulus =", b%c)
    elif a=="floor division":
        print("floor divison =",b//c)
    elif a=="power":
        print("power =",b**c)
    else:
        print("invalid input")

