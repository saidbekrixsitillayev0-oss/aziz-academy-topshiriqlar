s = 0
while (x := int(input())) != 0:
    if x < 0 : continue
    if x >= 100: break
    s += x
print(s)    