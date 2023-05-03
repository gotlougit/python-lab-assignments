import math

def discriminant(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    d = math.sqrt(d)
    return d

def real_roots(a: int, b: int, c: int) -> list[float]:
    d = discriminant(a,b,c)
    if d is None:
        return []
    return [((-b+d)/2*a), ((-b-d)/2*a)]

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

roots = real_roots(a,b,c)
if (len(roots) == 0):
    print("The roots do not exist!")
else :
    if (roots[0] == roots[1]):
        print("Roots are real and equal:", roots[0])
    else:
        print("Roots are real and distinct: ", roots[0], "and", roots[1])
