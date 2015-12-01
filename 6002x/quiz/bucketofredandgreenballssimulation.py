__author__ = 'anandran'

import random

def pickBall(bucket):
    choice = random.choice(bucket)
    bucket.remove(choice)
    return choice

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    identicalBallsOnTrials = 0
    bucket = [1,2,3,4,5,6]
    for i in range(numTrials):
        tempBucket = bucket[:]
        currentChoice=None
        ballsOfsameColours = 0
        for j in range(3):
            if(pickBall(tempBucket) < 4):
                choice = 'R'
            else:
                choice = 'G'
            if(currentChoice == None):
                currentChoice= choice
            elif(currentChoice == choice):
                ballsOfsameColours+=1
            else:
                break
        if(ballsOfsameColours == 2):
            identicalBallsOnTrials+=1
    return identicalBallsOnTrials/float(numTrials)

print drawing_without_replacement_sim(1000000)




