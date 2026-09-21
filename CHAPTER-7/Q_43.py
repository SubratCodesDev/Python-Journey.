b=int(input("Enter the number you want:"))
a=[20,34,24,67,35,78,90,19,38,]
i=0
while i<len(a):
    number = a[i]
    if number==b:
        print("Number found")
        break
    
    i=i+1
if i==len(a):
     print("Number not found")

