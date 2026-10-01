def sub(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
nn=int(input("Enter your number:"))
mm=sub(nn)
print(mm)

