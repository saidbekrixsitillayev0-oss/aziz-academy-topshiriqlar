n = int(input())
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("yo'q")
            break
    else:
        print("ha")    
else:     
    print("yo'q")