a={}
i=1
while i<=5:
    n=input("Enter your name:")
    nn=int(input("Enter yur number:"))
    a[n]=nn
    i=i+1
print(a)
n=input("Enter the student name:")
if a[n]>=35:
    print("The student is passed")
else:
    print("The student is failed")

