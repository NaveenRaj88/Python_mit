__author__ = 'anandran'

x = [1, 2, [3, 'John', 4], 'Hi']

print x.remove(2)

print x[0:1]

x[0] =8

print range(len(x))


aList = range(1, 6)
bList = aList
aList[2] = 'hello'

print aList == bList

print aList is bList

print aList


cList = range(6, 1, -1)
dList = []
for num in cList:
    dList.append(num)

print cList
print cList == dList
print cList is dList


listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

listA.sort

listA.sort()

print "*************"

print listA.pop(1)

print listA

listA.insert(0,100)

listB.sort()

print listB.pop()

print listB.count('a')

# print listB.remove('a')

print listA.extend([4, 1, 6, 3, 4])

print listA

# print listA.count(4)

print listA.index(1)

listA.pop(4)
listA.reverse()

print listA