import sys
result = 0
lines = sys.stdin.read().split()
for i in range(0, len(lines), 2):
    op = lines[i]
    if op == '=':
        break
    val = int(lines[i+1])    
    if op == '+':
        result += val 
    elif op == '-': 
        result -= val 
    elif op == '*':
        result *= val 
    elif op == '/':
        if val != 0:
            result //= val 
print(result)            