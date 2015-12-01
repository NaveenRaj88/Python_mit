__author__ = 'anandran'

x=12
def g(x):
    x=x+1
    def h(y):
        return x+y
    return h(6)

print(g(x))


def odd(x):
    return x % 2 ==0

print(odd(3))


def isVowel2(char):
    return char in 'aeiouAEIOU'

print isVowel2('z')