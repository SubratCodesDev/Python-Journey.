reverse=0
a=int(input("Enter your number:"))
while a>0:
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
print("Reverse =", reverse)
