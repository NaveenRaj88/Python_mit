__author__ = 'anandran'

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def absoluteValues(a):
    return abs(a)

applyToEach(testList, absoluteValues)

# print testList

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

print applyEachTo([inc, square, halve, abs], -3)

print(applyEachTo([inc, square, halve, abs], 3.0))

# print applyEachTo([inc, max, int], -3)

print (-3/2)