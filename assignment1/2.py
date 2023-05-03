import math

def cylinder_area_volume(radius, length):
    area = math.pi * (radius ** 2)
    volume = area * length
    return area, volume

radius = float(input("Enter the radius of the cylinder: "))
length = float(input("Enter the length of the cylinder: "))
area, volume = cylinder_area_volume(radius, length)
print("Area of the cylinder is: ", round(area, 2))
print("Volume of the cylinder is: ", round(volume, 2))
