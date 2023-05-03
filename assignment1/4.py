
def pound_to_kg(weight_in_pounds):
    weight_in_kg = weight_in_pounds * 0.454
    return weight_in_kg

weight_in_pounds = float(input("Enter the weight in pounds: "))
weight_in_kg = pound_to_kg(weight_in_pounds)
print("Weight in kilograms is: ", round(weight_in_kg, 2))
