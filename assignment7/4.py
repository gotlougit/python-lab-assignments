squared_numbers = [x**2 for x in range(1, 31)]
result = squared_numbers[:5] + squared_numbers[-5:]
print(result)
