import sys
n, *sonlar = map(int, sys.stdin.read().split())
print(sum(sonlar) // n)