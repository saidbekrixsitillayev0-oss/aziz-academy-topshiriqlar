quantity = int(input())
price_per_item = int(input())
total = quantity * price_per_item
total_with_tax = total + total // 10
print(total)
print(total_with_tax)