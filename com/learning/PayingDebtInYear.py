__author__ = 'anandran'

balance=3926
annualInterestRate=0.2
monthlyInterestRate = annualInterestRate/12.0
updatedBalance = balance
minPayment=0
minPaymentFound = False
while  minPaymentFound != True:
    currentMonth = 1
    minPayment= minPayment+10
    updatedBalance = balance
    while currentMonth <= 12:
        updatedBalance = updatedBalance - minPayment
        monthlyInterest = updatedBalance * monthlyInterestRate
        updatedBalance = updatedBalance+monthlyInterest
        currentMonth=currentMonth+1
    if updatedBalance <= 0 :
        break

print 'Lowest Payment: '+str(minPayment)


