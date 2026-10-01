def sub(n):
    j = 1
    largest = n[0]

    while j < len(n):
        if largest < n[j]:
            largest = n[j]
        j = j + 1

    return largest


d = []

i = 1
while i <= 5:
    dd = int(input("Enter your entry: "))
    d.append(dd)
    i = i + 1

nn = sub(d)

print(nn)
    