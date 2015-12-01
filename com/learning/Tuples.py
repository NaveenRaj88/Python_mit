__author__ = 'anandran'

t1 = (1, 'two',3)
print t1

def returnDiffThings(i):
    if i ==1:
        return True
    else:
        return i+1


x = (1, 2, (3, 'John', 4), 'Hi')
print x[2][-1]

print x[0:1]

print len(x)
print returnDiffThings(4)


def oddTuples(aTup):
    tupleSize = len(aTup)
    newTuple = ()
    i=0
    while i <tupleSize:
        if i % 2 == 0:
            newTuple = newTuple+(aTup[i],)
        i+=1
    return newTuple

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))