import sys
s, g = map(int, sys.stdin.read().split())
print("TOPDINGIZ" if g == s else "KATTA" if g > s else "KICHIK")