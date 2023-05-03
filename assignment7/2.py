l = []
while True:
    n = input("Enter element: ")
    if n != "":
        l.append(n)
    else:
        break

c = 0
for i in l:
    if len(i) > 1 and i[0] == i[-1]:
        c+=1
print(f"Count is {c}")
