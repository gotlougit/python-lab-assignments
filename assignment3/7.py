num = int(input("Enter a number: "))
divbyfive = not (num % 5)
divbysix = not (num % 6)

if (divbysix and divbyfive):
    print("Number is divisible by both 5 and 6")
elif (divbyfive):
    print("Number is divisible by 5 only")
elif (divbysix):
    print("Number is divisible by 6 only")
else:
    print("Number is divisible neither by 5 nor 6")
