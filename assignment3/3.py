import random

x = random.randint(1,101)
y = random.randint(1,101)

print("Numbers generated are:", x, "and", y)
guesssum = int(input("Enter their sum: "))

if (guesssum == x+y):
    print("Correct!")
else:
    print("Incorrect!")
