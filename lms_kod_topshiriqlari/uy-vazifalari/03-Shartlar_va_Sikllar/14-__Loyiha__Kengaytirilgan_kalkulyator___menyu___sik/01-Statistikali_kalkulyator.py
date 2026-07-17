import sys
d = list(map(int, sys.stdin.read().split()))
i = c = s = 0 
while i < len (d) and d[i] != 0:
    op, a, b = d[i:i+3]
    i += 3
    if 1 <= op <= 4 and not (op == 4 and b == 0):
        res = [0, a+b, a-b, a*b, a//b][op]
        print(res)
        c, s = c + 1, s + res
print(f"Amallar: {c}\nNatijalar yig'indisi: {s}")