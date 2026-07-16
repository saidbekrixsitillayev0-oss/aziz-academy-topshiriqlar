sanot = 0
while (n := int(input())) != 0:
    if n < 2:
        continue
    d = 2
    while d * d <= n:
        if n % d == 0:
            break
        d += 1
    else:
        sanot += 1
print(sanot)        