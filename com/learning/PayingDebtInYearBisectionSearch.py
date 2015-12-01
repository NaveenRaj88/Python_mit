__author__ = 'anandran'
balance=320000
annualInterestRate=0.2
monthlyInterestRate = annualInterestRate/12.0
updatedBalance = balance

def getCoumpoundInterestedPrinciple(principle,monthlyInterestRate):
    currentMonth = 1;
    while currentMonth <=12:
        principle = principle+principle*monthlyInterestRate
        currentMonth = currentMonth+1
    return principle

def getUpdatedBalanceAfterMinPayment(balance , guess, monthlyInterestRate):
    currentMonth = 1
    updatedBalance= balance
    while currentMonth <= 12:
        updatedBalance = updatedBalance-guess
        monthlyInterest = updatedBalance*monthlyInterestRate
        updatedBalance = updatedBalance +monthlyInterest
        currentMonth = currentMonth+1
    return updatedBalance

lowestPayment = (balance*annualInterestRate)/12.0
highestPayment = getCoumpoundInterestedPrinciple(balance,monthlyInterestRate)
while True:
    guessMinPayment = (highestPayment+lowestPayment)/2
    updatedBalance = getUpdatedBalanceAfterMinPayment(balance,guessMinPayment, monthlyInterestRate)
    if updatedBalance == 0 or (updatedBalance <0 and updatedBalance > -0.01):
        break
    if updatedBalance > 0:
        lowestPayment = guessMinPayment
    else:
        highestPayment = guessMinPayment
print 'Lowest Payment: '+str(round(guessMinPayment,2))