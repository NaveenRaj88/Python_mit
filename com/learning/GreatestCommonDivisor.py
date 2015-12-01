__author__ = 'anandran'


def gcdIter(a, b):
    if a>b:
        guess = b
    else:
        guess = a
    while guess > 1:
        if a%guess == 0 and b%guess ==0:
            break
        guess = guess-1
    return guess


#euclid formula
def gcdRecur(a, b):
    if b==0:
        return a
    return gcdRecur(b, a%b)

print gcdRecur(9,12)

print gcdIter(17,12)