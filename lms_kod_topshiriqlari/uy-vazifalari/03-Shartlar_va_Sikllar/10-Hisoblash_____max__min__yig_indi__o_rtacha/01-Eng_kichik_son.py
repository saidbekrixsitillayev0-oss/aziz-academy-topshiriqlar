n = int(input())
min_num = int(input())
for _ in range(n - 1):
    num = int(input())
    if num < min_num:
        min_num = num
print(min_num)        