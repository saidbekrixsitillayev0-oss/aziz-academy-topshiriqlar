import sys
print(next(i for i, x in enumerate(map(int, sys.stdin.read().split())) if x < 0))