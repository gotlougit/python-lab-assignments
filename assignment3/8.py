def getPerimeter(a: int, b: int, c: int) -> int:
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return -1

a = int(input("Enter first edge: "))
b = int(input("Enter second edge: "))
c = int(input("Enter third edge: "))

p = getPerimeter(a,b,c)
if p == -1:
    print("Invalid triangle")
else:
    print("Perimeter:", p)
