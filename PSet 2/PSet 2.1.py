annualInterestRate = 0.2
paid = 0
monthlyInterestRate = annualInterestRate / 12.0

for month in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance

    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = (monthlyUnpaidBalance * monthlyInterestRate) + monthlyUnpaidBalance

    paid += minimumMonthlyPayment

print("Remaining balance: " + str(round(balance, 2)))