secret = int(input())
attempts = 0
while (guess := int(input())) != secret:
    print("KATTA" if guess > secret else "KICHIK")
    attempts += 1
print(f"TOPDINGIZ\nUrinishlar: {attempts + 1}")