n=int(input("Enter your number:"))
a=0
b=1
count=0
while count<n:
    print(a,end="")
    next_num=a+b
    a=b
    b=next_num
    count=count+1


