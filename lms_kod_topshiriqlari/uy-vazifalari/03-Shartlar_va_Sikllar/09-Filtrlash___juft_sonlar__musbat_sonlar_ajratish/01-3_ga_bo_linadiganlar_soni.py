import sys
print(sum(int(x) % 3 == 0 for x in sys.stdin.read().split() [1:]))