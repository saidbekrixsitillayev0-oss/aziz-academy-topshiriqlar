secret = int(input())
score = 100
while (guess := int(input())) != secret:
    print("KATTA" if guess > secret else "KICHIK")
    score = max(0, score - 10)
print(f"TOPDINGIZ\nBall: {score}")    