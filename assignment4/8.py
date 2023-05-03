# Program to display monthly payment and balance of a loan

# Initialize the Principal Amount and Number of Years
amount = float(input("Enter the principle amount: "))
years = int(input("Enter the number of years: "))

# Calculate Monthly Interest Rate
rate = float(input("Enter the rate of interest in %: "))
monthly_rate = rate / (12 * 100)

# Compute Monthly Payment
monthly_payment = amount * monthly_rate / (1 - 1 / (1 + monthly_rate)**(years * 12))
monthly_payment = round(monthly_payment, 2)

# Prints Monthly Payment
print ("Monthly Payment: %.2f" %monthly_payment)

# Computes remaining balance after n payments
total_payment = 0

# You will have n payments
n = 1
print()
print("Payment# \t  Interest \t Principle \t Remain Balance")

# Loop to calculate remaining balance after each of the payment
while n <= years * 12:
    interest = round((monthly_rate * amount), 2)
    principal = round((monthly_payment - interest), 2)
    amount = round((amount - principal), 2)

    # To print the details of payment
    print(n, "\t\t", interest,"\t\t", principal,"\t\t", amount)
    n = n + 1

    # Calculates total payment
    total_payment += monthly_payment

# Prints final amount after making all the payments
print()
print("Remaining balance:", round((amount), 2))

# Prints Final Payment after making all the payments
print("Total Payment: %.2f" %total_payment)
