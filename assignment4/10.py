sampleset = list([i for i in range(1,8)])
combos = 0
for i in range(7):
    for j in range(i+1,7):
        print("{} {}".format(sampleset[i], sampleset[j]))
        combos += 1
print("Total number of combinations: {}".format(combos))
