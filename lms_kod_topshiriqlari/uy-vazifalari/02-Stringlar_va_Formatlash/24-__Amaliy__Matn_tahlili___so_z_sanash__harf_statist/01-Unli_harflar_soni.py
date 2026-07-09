matn = input().lower()
unlilar = "aeiou"
jami = sum(matn.count(harf) for harf in unlilar)
print(jami)