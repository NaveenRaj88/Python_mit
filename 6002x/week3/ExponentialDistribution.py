__author__ = 'anandran'

import pylab

# a drog action on body

def clear(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(numRemaining, label= 'Exponential decay')

clear(1000, 0.01, 500)
pylab.xlabel('Number of steps')
pylab.show()