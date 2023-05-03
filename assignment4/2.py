tuition = 10000

for i in range(10):
  tuition = tuition + (tuition * 0.05)

print("The tuition in ten years will be " + str(round(tuition, 2)) + ".")

totalcost = tuition
for i in range(3):
    tuition = tuition + (tuition * 0.05)
    totalcost += tuition

print("The total cost of four years' worth of tuition starting ten years from now will be " +  str(round(totalcost, 2)) + ".")
