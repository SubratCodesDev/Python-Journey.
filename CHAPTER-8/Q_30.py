def sub(n):
    if len(n) <= 1:
        return n
    return sub(n[1:]) +n[0]
mm=input("Enter your string:")
nn=sub(mm)
print("Reversed string",nn)

   
    
    
        