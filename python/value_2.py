def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    global my_price
    print("my_price(지역 버전):", my_price)
    return total

my_price = float(input("Enter a pricce: "))

totalPrice = calculateTax(my_price, 0.09)
print("price = ", my_price, "totalPrice =", totalPrice)
print("my_price(전역 버전): ", my_price)