kwh = int(input())

if kwh < 0:
    print("Noto'g'ri qiymat")
    
elif kwh <= 100:
    summa = kwh * 450
    print(summa)
    
elif kwh <= 200:
    summa = (100 * 450) + ((kwh - 100) * 600)
    print(summa)
    
else:
    summa = (100 * 450) + (100 * 600) + ((kwh - 200) * 900)
    print(summa)