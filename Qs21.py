price = float(input("Enter the price of the item: "))

if price > 1000:
    discount_price = price - (price * 0.20)
    print(f"New price after 20% discount: {discount_price:.2f}")
elif 500 <= price <= 1000:
    discount_price = price - (price * 0.10)
    print(f"New price after 10% discount: {discount_price:.2f}")
else:
    print(f"No discount. Price remains: {price:.2f}")