n = int(input())
teskari = 0
while n > 0:
    qoldi = n % 10
    teskari = teskari * 10 + qoldi
    n = n // 10
print(teskari)    