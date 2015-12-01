__author__ = 'anandran'

def a(x):
   return x + 1

# print(a(-5.3))

def b(q, r):
    return a(q>r, q, r)


def a(x, y, z):
     if x:
         return y
     else:
         return z

# x=3'a'
# print b(a,b)

# print a(3>2, a, b)

z = a(3>2, a, b)
# print z
# print a>b

# print b>a

stuff  = ["iQ"]
for thing in stuff:
    if thing == 'iQ':
        print "Found it"

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

# print Square(-3)

def evalQuadratic(a, b, c, x):
    return (a*(x*x))+(b*x)+c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    evalQuadratic(a1,b1,c1,x1)+evalQuadratic(a2,b2,c2,x2)

def primesList(N):
    i=2
    primeList=[]
    while i<=N:
        isPrime=True
        for j in range(2,i,1):
            if(i%j == 0):
                isPrime = False
                break
        if isPrime:
            primeList.append(i)
        i+=1
    return primeList

print primesList(11)

# print 8%10
x=8/10
# print x

def count7(N):
    if N == 0:
        return 0
    elif(N%10 ==7):
        return count7(N/10)+1
    else:
        return count7(N/10)

# print count7(8989)


def uniqueValues(aDict):
    dictNoDupValues={}
    for key in aDict.keys():
        existCount=0
        for value in aDict.values():
            if aDict.get(key) == value:
                existCount+=1
            if existCount >1:
                aDict.pop(key,None)
    sortedKeysList =  aDict.keys()
    sortedKeysList.sort()
    return sortedKeysList

def uniqueValues(aDict):
    valuesList = aDict.values()
    for value in valuesList:
        if valuesList.count(value)>1:
            for key in aDict.keys():
                if aDict.get(key)==value:
                    aDict.pop(key,None)
    sortedKeysList = aDict.keys()
    sortedKeysList.sort()
    return sortedKeysList

print uniqueValues({'a':3,'b':5,'c':3,'d':7,'t':5})


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for s in L:
        if not f(s):
            L.remove(s)
    return len(L)

def f(s):
    return 'a' in s


def satisfiesF(L):
    i=0
    while i <len(L):
        if not f(L[i]):
            L.remove(L[i])
        else:
            i+=1
    return len(L)

L = ['a', 'bca', 'a', 'abrakadabra', 'sdsdf', 'eers']
print satisfiesF(L)
print L


def satisfiesF(L):

   count= len(L)
   rec_list=list()

   for i in range(0,count):
     if(f(L[i])==False):
        rec_list.append(L[i])

   if(rec_list):
     for j in rec_list:
      L.remove(j)
   return len(L)

L = ['a', 'bca', 'a']
# print satisfiesF(L)
# print L

# run_satisfiesF(L, satisfiesF)

num = 5
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val