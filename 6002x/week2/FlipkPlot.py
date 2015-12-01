__author__ = 'anandran'

import random
import pylab

def flipPlot(minExp, maxExp):
    ratios=[]
    xAxis = []
    diffs =[]
    for i in range(minExp, maxExp+1):
        xAxis.append(2**i)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads+=1
        numTails = numFlips-numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads-numTails))
    pylab.title('Difference between heads and tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('ABS(#Heads-#Tails)')
    pylab.plot(xAxis,diffs)
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis,ratios)

    pylab.figure()
    pylab.title('Difference between heads and tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('ABS(#Heads-#Tails)')
    pylab.plot(xAxis,diffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis,ratios, 'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

random.seed(0)
flipPlot(4,20)