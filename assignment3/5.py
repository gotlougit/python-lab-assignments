def compare_prices(weight1: float, price1: float, weight2: float, price2: float) -> str:
    item1 = price1/weight1
    item2 = price2/weight2
    if item1 < item2:
        return "Package 1 has a better price."
    elif item2 < item1:
        return "Package 2 has a better price."
    else:
        return "Both packages have the same price."

weight1 = float(input("Enter the weight of Package 1 (in pounds): "))
price1 = float(input("Enter the price of Package 1: $"))
weight2 = float(input("Enter the weight of Package 2 (in pounds): "))
price2 = float(input("Enter the price of Package 2: $"))
result = compare_prices(weight1, price1, weight2, price2)

print(result)
