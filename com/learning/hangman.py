__author__ = 'anandran'

def isWordGuessed(secretWord, lettersGuessed):
    i=0
    tempLettersList = lettersGuessed[:]
    while i < len(secretWord):
        if secretWord[i] in tempLettersList:
            tempLettersList.remove(secretWord[i])
            i+=1
            continue
        else:
            return False
    return True


secretWord = 'apple'
lettersGuessed = ['z', 'p', 'l', 'p', 'e', 'a']
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print isWordGuessed(secretWord,lettersGuessed)

import string

def getGuessedWord(secretWord, lettersGuessed):
    i=0
    userGuess = ''
    finalTempLetterList=[]
    while i < len(secretWord):
        if secretWord[i] in lettersGuessed:
            userGuess=userGuess+secretWord[i]
        else:
            userGuess = userGuess+'_ '
        i+=1
    return userGuess


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print getGuessedWord(secretWord, lettersGuessed)


def getAvailableLetters(lettersGuessed):
    i =0
    alphabets = string.ascii_lowercase
    availableLetters=''
    while i < len(alphabets):
        if alphabets[i] not in lettersGuessed:
            availableLetters=availableLetters+alphabets[i]
        i+=1
    return availableLetters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print getAvailableLetters(lettersGuessed)






