print("Pattern A:")
for i in range(1,7):
    for j in range(1,i+1):
        print(j, end= "")
    print()
print("Pattern B:")
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j, end= "")
    print()
print("Pattern C:")
for i in range(1,7):
    for k in range(6-i):
        print(" ", end = "")
    for j in range(i,0,-1):
        print(j, end= "")
    print()
print("Pattern D:")
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j, end= "")
    print()
