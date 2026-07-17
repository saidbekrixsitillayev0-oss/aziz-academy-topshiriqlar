n = int(input())
s = []    
for i in range(n):
    x = int(input())
    if x % 2:
        s.append(x)
s.sort()
print(*s)