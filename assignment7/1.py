l = []
while True:
    n = input("Enter number: ")
    if n != "":
        n = int(n)
        l.append(n)
    else:
        break

ans = 1
for i in l:
    ans = ans * i
print(f"Multiplication result is: {ans}")
