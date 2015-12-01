__author__ = 'anandran'

def semordnilap(str1, str2):
    strLength1 = len(str1)
    strLength2 = len(str2)
    if strLength1 != strLength2:
        return False
    if len(str1) == 0:
        return True
    if str1[0] == str2[strLength2-1]:
        return semordnilap(str1[1:], str2[:strLength2-1])
    else:
        return False


def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

print testFib(10)

# print semordnilap('nametag', 'gateman')