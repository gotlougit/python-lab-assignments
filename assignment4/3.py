divisibles = []
for i in range(100,1001):
    if i % 5 == 0 and i % 6 == 0:
        divisibles.append(i)
counter = 0
for i in divisibles:
    print(i,end=" ")
    counter+=1
    if counter == 10:
        counter = 0
        print()
