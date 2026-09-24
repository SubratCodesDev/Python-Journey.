a=[]
i=1
while i<=5:
    aa=int(input("Enter your number:"))
    a.append(aa)
    i=i+1
b=tuple(a)
print(b)
co=int(input("enter the number you want to count:"))
ind=int(input("Enter the number you want to index:"))
print(b.count(co))
print(b.index(ind))