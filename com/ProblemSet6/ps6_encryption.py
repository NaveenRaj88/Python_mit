# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    coderDict={}
    upperCaseString = string.ascii_uppercase
    for i in upperCaseString:
        coderDict[i]=upperCaseString[(upperCaseString.index(i)+shift)%len(upperCaseString)]
    lowerCaseString = string.ascii_lowercase
    for i in lowerCaseString:
        coderDict[i]=lowerCaseString[(lowerCaseString.index(i)+shift)%len(lowerCaseString)]
    return coderDict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    cipherText = ''
    for char in text:
        if char in coder:
            cipherText=cipherText+coder[char]
        else:
            cipherText=cipherText+char
    return cipherText

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    highestMatchedCount = 0
    bestShift =0
    for i in range(25,0,-1):
        wordsMatched =0
        decryptedString = applyShift(text,i)
        decryptedList = decryptedString.split(' ')
        for w in decryptedList:
            if isWord(wordList,w):
                wordsMatched +=1
        if wordsMatched > highestMatchedCount:
            highestMatchedCount = wordsMatched
            bestShift = i
    return bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    encryptedStory = getStoryString()
    shift = findBestShift(wordList,encryptedStory)
    return applyShift(encryptedStory,shift)


#
# Build data structures used for entire session and run encryption
#

print decryptStory()

# if __name__ == '__main__':
#     # To test findBestShift:
#     wordList = loadWords()
#     s = applyShift('Hello, world!', 8)
#     bestShift = findBestShift(wordList, s)
#     assert applyShift(s, bestShift) == 'Hello, world!'
#     # To test decryptStory, comment the above four lines and uncomment this line:
#     #    decryptStory()
#
# print string.punctuation
#
# print string.ascii_letters