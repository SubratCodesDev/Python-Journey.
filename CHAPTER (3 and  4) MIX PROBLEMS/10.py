a=[]
i=1
while i<=5:
    aa=input("ENTER YOUR NAME:")
    a.append(aa)
    i=i+1
print(a)
a[2]="subrat"
print(a)
a.sort()
print(a)
print(a[0],a[-1])