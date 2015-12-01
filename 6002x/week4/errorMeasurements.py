__author__ = 'anandran'

import random,pylab

def testErrors(ntrials=10000, npts=100):
    results = []
    for i in xrange(ntrials):
        s=0
        for j in xrange(npts):
            s+=random.uniform(-1,1)
        results.append(s)

    #plot the graph
    pylab.hist(results,bins=50)
    pylab.title("sum of 100 random points -- triangular PDF (10000 trials)")
    pylab.xlabel('sum')
    pylab.ylabel('num of trials')


testErrors()
pylab.show()