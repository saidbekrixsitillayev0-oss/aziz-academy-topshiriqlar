tanlov = int(input())
n = int(input())
if tanlov == 1:
    minut = n // 60
    soniya = n % 60
    print(f"{minut} minut {soniya} soniya")
elif tanlov == 2:
    soat = n // 60
    minut = n % 60
    print(f"{soat} soat {minut} minut")
else:
    print("Notogri tanlov")