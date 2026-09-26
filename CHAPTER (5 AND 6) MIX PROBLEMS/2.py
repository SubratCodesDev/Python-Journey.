a=set()
b=set()
i=1
while i<=5:
    n=int(input("Enter your number for set a:"))
    nn=int(input("Enter your number for set b:"))
    a.add(n)
    b.add(nn)
    i=i+1
print(a)
print(b)
aa=a.union(b)
bb=a.intersection(b)
print(aa)
if print(bb)==0:
    print("yes intersection is empty")
else:
    print("Intersection is not empty")