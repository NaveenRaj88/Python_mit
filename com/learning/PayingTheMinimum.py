__author__ = 'anandran'

print 2/100

balance=4842
annualInterestRate=0.2
monthlyPaymentRate=0.04
currentMonth = 1;
monthlyInterestRate = (annualInterestRate)/12.0
totalPaid =0;
while currentMonth <=12:
    minMonthlyPayment = balance*monthlyPaymentRate
    balance = balance-minMonthlyPayment
    interest = balance*monthlyInterestRate
    balance = balance+interest
    totalPaid = totalPaid+minMonthlyPayment
    print 'Month: '+str(currentMonth)
    print'Minimum monthly payment: '+str(round(minMonthlyPayment,2))
    print'Remaining balance: '+str(round(balance, 2))
    currentMonth = currentMonth+1
print 'Total paid: '+str(round(totalPaid,2))
print 'Remaining balance: '+str(round(balance,2))
