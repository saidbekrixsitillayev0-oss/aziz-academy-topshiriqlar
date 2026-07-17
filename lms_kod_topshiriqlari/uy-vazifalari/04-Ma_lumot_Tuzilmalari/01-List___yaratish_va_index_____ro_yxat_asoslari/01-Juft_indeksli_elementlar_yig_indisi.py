a = list(map(int, input().split()))
s = 0
for i in range(0, len(a), 2):
    s += a[i]
print(s)