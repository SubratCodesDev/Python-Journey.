a={1,3,1,2,2,3}
bb=set()
print(a)
b=int(input("Enter your number you want to check:"))
bb.add(b)
print(bb)
ss=a.intersection(bb)
print(ss)
if ss==0:
    print("The number is presnt in the set")
else:
    print("The number is not present in the set")