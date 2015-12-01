__author__ = 'anandran'
a=1
b=2
d = {}
d[a] = 0
d[b] = d[a]


L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3

# for i in range(10000001, -1, -2):
#     print f


def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        iteration += 1
    return lst

def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed

    return lst

sort2([3,6,1,5,7,0,2,9])


def getSublists(L, n):
    flag = True;
    breakLen= len(L)-n+1
    subList = []
    for i in range(0,breakLen):
        subList.append(L[i:i+n])
    return subList

# getSublists([1,1,1,1,4],2)
#
# getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2],4)

def longestRun(L):
    foundFlad = False;
    for n in range(len(L),1,-1):
        subList = getSublists(L,n);
        for list in subList:
            if isListSorted(list):
                return n
    return 1

def isListSorted(list):
    print list
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

print longestRun([0])

# print longestRun([10, 4, 3, 4, 5, 7, 7, 2])
#
# print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])