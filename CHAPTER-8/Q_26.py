def sub(n):
    i=1
    digits=0
    while i<=n:
        digits=i+digits
        i=i+1
    return digits
n=int(input("Enter the number you want to do sum:"))
mm=sub(n)
print(mm)
