i=1
a=[]
while i<=5:
    aa=input("enter your word:")
    a.append(aa)
    i=i+1
print("Original lis =",a)
a[2]="subrat"
print("After replacement =",a)
print(a[2][0:3])