a=2
while a<=100:
    i=2
    prime=True
    while i<a:
        if a%i==0:
            prime=False
            break
        i=i+1
    if prime:
        print(a)
    a=a+1
