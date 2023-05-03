for i in range(6):
    for j in range(10-2*i):
        print(end = " ")
    for j in range(i):
        print(2**j, end = " ")
    for j in range(i, -1, -1):
        print(2**j, end = " ")
    print()
