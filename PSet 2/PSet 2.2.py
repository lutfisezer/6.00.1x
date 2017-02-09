balance = 0
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = 10
monthlyPayment = minimumMonthlyPayment

while True:
    monthlyUpdatedBalance = balance
    for month in range(1, 13):
        monthlyUnpaidBalance = monthlyUpdatedBalance - monthlyPayment
        monthlyUpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    if monthlyUpdatedBalance <= 0:
        break
    else:
        monthlyPayment += minimumMonthlyPayment

print("Lowest Payment: " + str(monthlyPayment))