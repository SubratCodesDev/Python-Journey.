def sub(n,m,v):
    if n >= m and m>=v:
        return n
    elif m >= n and m >= v:
        return m
    else:
        return v
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
dd=sub(num1,num2,num3)
print(dd)    




