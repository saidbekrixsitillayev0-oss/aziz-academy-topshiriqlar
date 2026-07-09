email, parol = input(), input()
print(('@' in email) and ('.' in email) and (email == email.lower()) and (8 <= len(parol) <= 16))