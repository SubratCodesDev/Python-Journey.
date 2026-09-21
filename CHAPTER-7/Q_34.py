n=int(input("Enter your number:"))
count=0
while n>0:
    digit=n%10
    if digit>count:
        count=digit
    n=n//10
print(count)
    

