# Program to calculate Loan Payments

# Get Input from user
loan_amount = float(input('Enter the loan amount: '))
loan_period = int(input('Enter the loan period (in number of years): '))

# Calculate and print payments for interest rates from 5% to 8%
interest_rate = 5.0
while interest_rate <= 8.0:
    monthly_payment = loan_amount * ((interest_rate/100/12) /
                        (1 - (1 + (interest_rate/100/12)) ** (-loan_period*12)))
    total_payment = monthly_payment * loan_period * 12
    print('Interest Rate: {:.1f}%'.format(interest_rate))
    print('Monthly Payment: ${:.2f}'.format(monthly_payment))
    print('Total Payment: ${:.2f}'.format(total_payment))
    print()
    interest_rate += 0.125
