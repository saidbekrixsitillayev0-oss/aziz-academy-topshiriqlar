import sys
start, step = map(int, sys.stdin.read().split())
if step <= 0 and start < 100:
    print("CHEKSIZ")
else:
    print(max(0, (100 - start + step - 1) // step) if step > 0 else 0)