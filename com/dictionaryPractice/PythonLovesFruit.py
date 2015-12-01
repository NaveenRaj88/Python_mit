__author__ = 'anandran'

def nfruits(fruitsContainer, fruitsEatenPattern):
    strLen = len(fruitsEatenPattern)
    i=0
    while i < strLen:
        eatenKey = fruitsEatenPattern[i]
        fruitsContainer[eatenKey] = fruitsContainer.get(eatenKey)-1
        for eachFruit in fruitsContainer.keys():
            if(eachFruit != eatenKey and i != strLen-1):
                fruitsContainer[eachFruit] = fruitsContainer.get(eachFruit)+1
        i+=1
    maxFruitsInContainer= 0
    for fruitsRemaining in fruitsContainer:
        if(fruitsContainer[fruitsRemaining] > maxFruitsInContainer):
            maxFruitsInContainer = fruitsContainer[fruitsRemaining]
    return maxFruitsInContainer

nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC')

nfruits({'A': 5, 'B': 7, 'C': 8, 'D': 11, 'E': 4}, 'AAABBBEECAAABBAACCAADDBBAACDCAAABBBAEACCAEADABCB')