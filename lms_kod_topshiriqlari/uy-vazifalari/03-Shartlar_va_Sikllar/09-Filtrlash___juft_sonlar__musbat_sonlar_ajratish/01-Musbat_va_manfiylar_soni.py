import sys
sonlar = [int(x) for x in sys.stdin.read().split()[1:]]
print(sum(x > 0 for x in sonlar), sum(x < 0 for x in sonlar))