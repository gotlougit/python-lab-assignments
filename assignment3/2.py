a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))
e = int(input("Enter e:"))
f = int(input("Enter f:"))

if (a*d == b*c):
    if (a/c == b/d and b/d == e/f):
        print("Infinite solutions exist!")
    else:
        print("No solution exists")
else:
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    print("x is", x, "and y is", y)
