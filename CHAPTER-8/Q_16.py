def sub(n):
    if n<2:
        return False
    i=2
    while i<n:
        if n%i==0:
            return False
        i=i+1
    return True
nn=int(input("Enter the number:"))
mm=sub(nn)
if mm :
    print(nn,"is a prime number")
else:
    print(nn,"is not a prime number")
