a=int(input("Enter your year:"))
b=int(input("Enter your year:"))
while a<=b:
    
    if a%400==0 or(a % 4 == 0 and a % 100 != 0):
        print(a)
    a=a+1
