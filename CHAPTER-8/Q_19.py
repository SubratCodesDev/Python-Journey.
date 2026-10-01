def sub(n):
    reverse=0
    while n>0:
        num=n%10
        reverse=reverse*10+num
        n=n//10
    return reverse
mm=int(input("Enter your number:"))
nn=sub(mm)
if nn==mm:
    print("yes,this is palindrome")
else:
    print("no,this is not palindrome")
