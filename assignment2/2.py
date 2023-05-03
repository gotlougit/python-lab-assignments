import math
length = int(input("Enter side length of pentagon: "))
area = (5 * (length**2)) / (4*math.tan(math.pi/5))
print("Area is:", area)
