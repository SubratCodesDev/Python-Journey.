def sub(n,a):
    if a>10:
        return
    print(n,"*",a,"=",n*a)
    sub(n, a + 1)
sub(9,1)
    
