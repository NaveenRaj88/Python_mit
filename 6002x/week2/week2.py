__author__ = 'anandran'

def stdDevOfLengths(L):
    if  len(L) == 0:
        return float('NaN')
    mean =0
    total = 0
    for i in L:
        total = total+len(i)
    mean = total/float(len(L))
    varianceTotal = 0
    for i in L:
        varianceTotal = varianceTotal+(len(i)-mean)**2
    variance = varianceTotal/float(len(L))
    stdDeviation = variance**0.5
    return stdDeviation

print stdDevOfLengths(['a', 'z', 'p'])
print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])


def stdDevOfInts(L):
    if  len(L) == 0:
        return float('NaN')
    mean =0
    total = 0
    for i in L:
        total = total+i
    mean = total/float(len(L))
    varianceTotal = 0
    for i in L:
        varianceTotal = varianceTotal+(i-mean)**2
    variance = varianceTotal/float(len(L))
    stdDeviation = variance**0.5
    return stdDeviation

print stdDevOfInts([1,2,3])
print stdDevOfInts([11,12,13])
print stdDevOfInts([0.1,0.1,0.1])

def coeffOfVariation(L):
    total = 0
    for i in L:
        total = total+i
    mean = total/len(L)
    stdDeviation = stdDevOfInts(L)
    coeffOfVar = stdDeviation/mean
    return coeffOfVar

print 'coeff'
print coeffOfVariation([10, 4, 12, 15, 20, 5] )