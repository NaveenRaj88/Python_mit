import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def getNoOfVowel(word):
    vowel = 'aeiou'
    noOfVowel = 0
    for v in vowel:
        noOfVowel = noOfVowel+word.count(v)
    return float(noOfVowel)

def getvowelToWordRatios(word):
    return getNoOfVowel(word)/float(len(word))

def stdDev(L):
    mean = sum(L)/float(len(L))
    stdMean = 0
    for ratio in L:
        stdMean = stdMean + ((ratio-mean)**2)
    stdDev =stdMean/float(len(L))
    return stdDev**0.5


def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowelPropotion=[]
    for word in wordList:
        vowelPropotion.append(getvowelToWordRatios(word))
    mean = sum(vowelPropotion)/float(len(vowelPropotion))
    sd = stdDev(vowelPropotion)

    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    pylab.hist(vowelPropotion, numBins)
    pylab.title('Vowel Proportion of ' + str(len(wordList)) +' words')
    pylab.xlabel('Vowel Proportion')
    pylab.ylabel('Number of Words')
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))
    pylab.plot
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
