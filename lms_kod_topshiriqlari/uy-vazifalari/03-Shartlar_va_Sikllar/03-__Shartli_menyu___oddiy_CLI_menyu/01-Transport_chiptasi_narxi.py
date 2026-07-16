t = (input().strip())
if t in ('1', '2', '3'):
    k = input()
    if k in ('1', '2', '3',):
        narx = 1700 if t != '3' else 4000
        print(narx if k == '1' else (narx // 2 if k == '2' else 0))
    else:
        print("Notogri toifa")
else:
    print("Notogri transport")    