import sys
d = sys.stdin.read().split()
print(sum(map(int, d[:d.index('stop')])))