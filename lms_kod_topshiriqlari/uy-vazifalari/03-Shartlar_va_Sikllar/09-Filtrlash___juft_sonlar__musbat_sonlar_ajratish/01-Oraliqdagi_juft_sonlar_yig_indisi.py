a, b = int(input()), int(input())
print(sum(x for x in range(a, b + 1) if x % 2 == 0))