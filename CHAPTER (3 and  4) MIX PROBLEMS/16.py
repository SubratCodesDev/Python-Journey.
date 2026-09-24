w=[]
i=1
while i<=10:
    ww=input("Enter your number:")
    w.append(ww)
    i=i+1
dd=tuple(w)
print(dd)
n=input("Enter your number you want to count:")
cc=dd.count(n)
print(cc)
ss=dd.index(n)
print(ss)
print(w[0:6])
