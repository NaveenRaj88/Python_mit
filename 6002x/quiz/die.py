__author__ = 'anandran'


import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if(title != None):
        pylab.title(title)
    # pylab.plot()
    pylab.show()

# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestRuns=[]
    for i in range(numTrials):
        longestRuninRoll=0
        runInRollCounter = 0
        currentRoll=0
        for j in range(numRolls):
            roll = die.roll()
            if(currentRoll == 0):
                currentRoll = roll
                runInRollCounter+=1
            elif(currentRoll == roll):
                runInRollCounter+=1
            else:
                currentRoll = roll
                runInRollCounter =1
            if(runInRollCounter > longestRuninRoll):
                longestRuninRoll = runInRollCounter
        longestRuns.append(longestRuninRoll)
    makeHistogram(longestRuns,10, 'longestRun', 'frequency of longest runs over the trials')
    mean = sum(longestRuns)/float(numTrials)
    return mean


# One test case
# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)

# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 10)

# print getAverage(Die([1]), 10, 1000)

# print getAverage(Die([1,1]), 10, 1000)

print getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000)


# makeHistogram([1,2,3,3,3,3,3,4,5,6], 2, '', '','')