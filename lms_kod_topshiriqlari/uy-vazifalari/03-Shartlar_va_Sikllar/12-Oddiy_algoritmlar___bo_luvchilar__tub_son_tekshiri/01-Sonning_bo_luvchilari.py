n = int(input())
boluvchilar = []
for i in range(1, n + 1):
    if n % i == 0:
        boluvchilar.append(i)
print(*boluvchilar)