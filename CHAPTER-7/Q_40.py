n=int(input("Enter your number:"))
i=1
count=n
while i<=n:
    j=1
    while j<=count:
        if i == 1 or i == count:
            print("*",end="")
        elif j == 1 or j == count:
            print("*", end="")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1
        

      


   