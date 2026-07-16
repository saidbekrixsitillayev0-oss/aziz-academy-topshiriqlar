secret = int(input())
limit = int(input())
for _ in range(limit):
    if (guess := int(input())) == secret:
        print("TOPDINGIZ")
        break
    print("KATTA" if guess > secret else "KICHIK")    
else: 
    print("YUTQAZDINGIZ")