drink = input()
count = int(input())
def calculate_total_price(drink, count):
    if drink == "coffee":
        price = 1.50
    elif drink == "coke":
        price = 1.40
    elif drink == "water":
        price = 1.00
    elif drink == "snacks":
        price = 2.00
    else:
        price = 0.00
    result = price * count
    return result
total_price = calculate_total_price(drink, count)
print(f"{total_price:.2f}")