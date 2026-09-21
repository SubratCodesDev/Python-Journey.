n=int(input("Enter your number:"))
original=n
temp=n
digits=0
while temp>0:
     digits = digits + 1
     temp = temp // 10
n=original
count=0
while n>0:
    digit=n%10
    count=count+digit**digits
    n=n//10
if count==original:
     print("yes this is a armstrong number")
else:
     print("This is not a armstrong number")



