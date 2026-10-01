def sub(n):
    count=0
    i=0
    while i<len(n):
        if n[i] in "aieouAEIOU":
            count=count+1
        i=i+1
    return count
n=input("Enter your string:")
mm=sub(n)
print(mm)