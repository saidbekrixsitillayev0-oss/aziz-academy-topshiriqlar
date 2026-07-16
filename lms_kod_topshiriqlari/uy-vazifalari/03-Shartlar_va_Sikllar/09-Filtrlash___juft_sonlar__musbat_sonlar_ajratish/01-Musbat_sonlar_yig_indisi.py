n = int(input())
print(sum(x for i in range(n) if (x := int(input())) > 0))