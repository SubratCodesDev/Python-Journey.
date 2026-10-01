def sub(n):
    largest = 0
    while n > 0:
        value = n % 10

        if value > largest:
            largest = value

        n = n // 10

    return largest

nn = int(input("Enter your number: "))
mm = sub(nn)
print(mm)