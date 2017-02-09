balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12.0
upperBound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
epsilon = 0.01

while True:
    monthlyUpdatedBalance = balance
    monthlyPayment = (lowerBound + upperBound) / 2.0
    for month in range(1, 13):
        monthlyUnpaidBalance = monthlyUpdatedBalance - monthlyPayment
        monthlyUpdatedBalance = (monthlyUnpaidBalance * monthlyInterestRate) + monthlyUnpaidBalance
    if ((monthlyUpdatedBalance >= 0) and (monthlyUpdatedBalance <= epsilon)):
        break
    elif (monthlyUpdatedBalance > epsilon):
        lowerBound = monthlyPayment
    elif (monthlyUpdatedBalance < 0):
        upperBound = monthlyPayment

print('Lowest Payment: ' + str(round(monthlyPayment, 2)))