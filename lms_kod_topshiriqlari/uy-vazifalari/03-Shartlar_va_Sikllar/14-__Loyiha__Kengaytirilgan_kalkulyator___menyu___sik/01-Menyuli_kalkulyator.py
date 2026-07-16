while op := int(input()):
    a, b = int(input()), int(input())
    if op == 4 and b == 0:
        print("Xato")
    elif 1 <= op <= 4:
        print([0, a + b, a - b, a * b, a // b][op])
    else:
        print("Noma'lum")