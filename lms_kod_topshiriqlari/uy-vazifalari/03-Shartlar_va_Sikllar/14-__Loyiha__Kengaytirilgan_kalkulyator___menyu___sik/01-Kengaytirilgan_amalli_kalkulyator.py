import sys
d = list(map(int, sys.stdin.read().split()))
i, res_list = 0, []
while i < len(d) and d[i] != 0:
    op, a, b = d[i:i+3]
    i += 3
    if 1 <= op <= 6 and not (op in (4, 6) and b == 0):
        r = [0, a+b, a-b, a*b, a//b, a**b, a%b][op]
        print(r)
        res_list.append(r)
if res_list:
    print(f"Eng katta natija: {max(res_list)}")