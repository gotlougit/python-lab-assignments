import math
length = int(input("Enter length from center of pentagon to vertex: "))
s = 2*length*math.sin(math.pi / 5)
area = 1.5 * math.sqrt(3) * (s**2)
print("Area is:", area)
