__author__ = 'anandran'
import pylab
# You may have to change this path
WORDLIST_FILENAME = "words.txt"
wordList = []#list of strings

VOWELS = 'AEIOU'
VowelProportion=[]



#-------- Returns a list of valid words. Words are strings of uppercase letters.
#----- Depending on the size of the word list, this function may take a while to
#----------------------------------------------------------------------- finish.
def loadWords():
    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)#file

    for line in inFile:
        wordList.append(line.strip().lower())

    print "  ", len(wordList), "words loaded."


def labelPlot(vowelProp, mean, sd):
    pylab.title('Vowel Proportion of ' + str(len(wordList)) +' words')
    pylab.xlabel('Vowel Proportion')
    pylab.ylabel('Number of Words')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

#-------- Plots a histogram of the proportion of vowels in each word in wordList
#--------------------------------- using the specified number of bins in numBins
def plotVowelProportionHistogram(wordList, numBins=15):

    print "getting the proportion of vowels in each word..."

    VowelProportion = []
    mean = 0.0

    for iWord in range(len(wordList)):
        word = wordList[iWord].upper()
        VowelProportion.append(0)

        for vowel in VOWELS:
            VowelProportion [iWord] += word.count(vowel)

        VowelProportion[iWord] = float(VowelProportion[iWord])/float(len(word))
        mean += VowelProportion[iWord]

    mean = mean / len(wordList)

    print "plotting..."

    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    pylab.hist(VowelProportion, numBins)
    labelPlot(wordList, mean, stdDev(VowelProportion))


    pylab.figure()
    pylab.xlim(0.5, 1)
    pylab.hist(VowelProportion, numBins)

    pylab.figure()
    pylab.xlim(0, 0.5)
    pylab.hist(VowelProportion, numBins)

    pylab.show()

if __name__ == '__main__':
    loadWords()
    plotVowelProportionHistogram(wordList)