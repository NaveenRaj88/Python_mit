__author__ = 'anandran'

# animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
#
# animals['d'] = 'donkey'
#
# animals['a'] = 'anteater'
# animals['a']
#
# print 'donkey' in animals.values()
#
# print animals.keys()
# print len(animals['a'])
# # print animals['donkey']
#
# del animals['b']
# print len(animals)
# print animals.values()


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    totalAnimals = 0
    for values in aDict.values():
        totalAnimals = totalAnimals+len(values)
    return totalAnimals

def biggest(aDict):
    biggestKey=None
    biggestNumber=0
    for keys in aDict.keys():
        if len(aDict[keys])>biggestNumber:
            biggestNumber = len(aDict[keys])
            biggestKey=keys
    return biggestKey

print biggest(animals)