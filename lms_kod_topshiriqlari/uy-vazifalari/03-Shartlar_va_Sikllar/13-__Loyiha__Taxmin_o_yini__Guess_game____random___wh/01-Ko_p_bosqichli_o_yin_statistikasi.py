r = int(input())
results = []
for i in range(1, r + 1):
        secret = int(input())
        attempts = 1
        while int(input()) != secret:
            attempts += 1
        results.append(attempts) 
        print(f"Round {i}: {attempts} urinish")
print(f"Jami: {sum(results)}\nEng yaxshi: {min(results)}")