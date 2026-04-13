# Conditional discount system
prices = [100, 200, 300, 400]

# Apply 10% discount only if price > 200
updated_prices = [p * 0.9 if p > 200 else p for p in prices]

print(updated_prices)