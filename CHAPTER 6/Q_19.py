a=int(input("enter your mark:"))
if a< 0 or a>100:
    print(" invalid input")
elif a>=90:
    print("grade is ex")
elif a>=80:
    print(" garde is A")
elif a>=70:
    print("grade is B ")
elif a>=60:
    print("grade is C")
elif a>=50:
    print("grade is D")
else:
    print("grade is F")