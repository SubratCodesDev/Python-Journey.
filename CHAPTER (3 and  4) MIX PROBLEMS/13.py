s=[]
i=1
while i<=5:
    a=input("Enter your word:")
    s.append(a)
    i=i+1
print("ORIGINAL LIST =",s)
s.sort()
print("SORTED LIST =",s)
s.reverse()
print("REVERSED LIST =",s)
print(s[0:3])