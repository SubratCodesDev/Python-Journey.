def sub(d,mmm):
    d.remove(mmm)
    return d
d=[]
i=1
while i<=5:
    nn=int(input("Enter the number to create the list:"))
    d.append(nn)
    i=i+1
print(d)
mmm=int(input("Enter the number you want to remove from the list:"))
floaat=sub(d,mmm)
print(floaat)