n=int(input("Enter your number:"))
count=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if count==reverse:
    print(count,"=","YES this is a palindrome number")
else:
    print(count,"=","NO this is not a palindrome number")
