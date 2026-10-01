def sub(n):
    if n>20:
        return
    if n%2==0:
        print(n)
    sub(n+1)
sub(1)