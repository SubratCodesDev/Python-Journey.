i=1
a=int(input("enter your number:"))
count=0
while i<=a:
    if a%i==0:
        count = count + 1
    i=i+1
if count==2:
    print("This is a prime number")
else:
    print("This is not a prime number")
