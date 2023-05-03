def hex_to_decimal(char: str) -> int:
    return int(char, 16)

char = input("Enter a hex character: ")
print("Decimal equivalent:", hex_to_decimal(char))
