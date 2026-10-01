def sub(n):
    i=1
    d=0
    while i<=n:
        j=1
        while j<=i:
            print("*",end="")
            j=j+1
        print()
        i=i+1
n = int(input("Enter the number of lines: "))
sub(n)