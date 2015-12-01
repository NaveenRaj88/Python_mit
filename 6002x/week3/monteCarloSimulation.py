__author__ = 'anandran'

import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    noOfTimesSameColBall=0
    ballBag=[1,2,3,4,5,6]
    for i in range(numTrials):
        curBag = ballBag[:]
        ballColour=None
        ballCount=0
        for i in range(3):
            ball = getBall(curBag)
            if (ballColour==None):
                ballColour=ball
            if(ball == ballColour):
                ballCount+=1
            else: break
        if(ballCount == 3):
            noOfTimesSameColBall+=1
    return noOfTimesSameColBall/float(numTrials)

def getBall(bag):
    ball = random.choice(bag)
    bag.remove(ball)
    if ball <=3:
        return 'R'
    else: return 'G'


# bag = [1,2,3,4]
# ball = getBall(bag)
# print ball
# print getBall(bag)

# print random.choice(['R','G'])
print noReplacementSimulation(100)