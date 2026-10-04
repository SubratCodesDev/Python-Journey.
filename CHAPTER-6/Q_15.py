pin=input("enter your pin:")
if pin=="1111":
    a=input('''WELCOME SIR
    Would you like to 
    1.check balance 
    2.withdraw your cash
    :''')
    if a=="1":
        print("your total balance is = 70000")
    elif a=="2":
        c=int(input("put your withdraw  amount:"))
        b=70000
        aa=b-c
        if c<=b and c>=0:
            print("sucessufully withdraw  amount", c," and Balance remained is",aa)
        elif c>b:
            print("insufficent balance")              
        else:
            print("invaid amount ")

    else:
        print("invalid request")
else:
    print('''incorrect pin try agian''')