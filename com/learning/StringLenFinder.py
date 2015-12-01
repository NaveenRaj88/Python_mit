__author__ = 'anandran'

def lenIter(aStr):
    c=''
    lengthOfStr=0
    while c in aStr:
        lengthOfStr=lengthOfStr+1
    return lengthOfStr

# recursiveway
def lenRecur(aStr):
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])

# Bisection searching of a string1
def isIn(char, aStr):
    strLength = len(aStr)
    lowest = 0
    highest = strLength
    if strLength ==0:
        return False
    if strLength==1:
        return char == aStr
    mid = strLength/2
    if char == aStr[mid]:
        return True
    elif char > aStr[mid]:
        lowest = mid+1
    else:
        highest = mid
    return isIn(char, aStr[lowest:highest])

print isIn('z', 'dhoov')
print isIn('a', '')
print isIn('z', 'abcdefghijklmnop')

print lenRecur('able')

print len('able')