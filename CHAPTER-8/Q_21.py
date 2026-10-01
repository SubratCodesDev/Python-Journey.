def sub(n):
    num=0
    while n>0:
        n=n//10
        num=num+1
    return num
nn=int(input("Enter your number:"))
mm=sub(nn)
print(mm)

