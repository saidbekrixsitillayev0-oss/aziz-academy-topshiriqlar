n, t = int(input()), int(input())
print(sum((i * j) % t == 0 for i in range(1, n + 1) for j in range(1, n + 1)))