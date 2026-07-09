N = int(input())
juft_sonlar = []
for i in range(N):
    son = int(input())
    if son % 2 == 0:
        juft_sonlar.append(son)
for son in juft_sonlar:
    print(son)