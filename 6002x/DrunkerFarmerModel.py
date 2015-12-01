__author__ = 'anandran'

class Location():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltax,deltay):
        return Location(self.x+deltax, self.y+deltay)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distanceFrom(self, other):
        ox = other.getx()
        oy = other.gety()
        xDist = self.x-ox
        yDist = self.y-oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<'+str(self.x)+ ', '+ str(self.y)+'>'


class Field():

    def __init__(self):
        self.drunks={}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk]=loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')

        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk]=currentLocation.move(xDist,yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random,math


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =[(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials = 20):
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print ' Mean =', sum(distances)/len(distances)
        print ' Max =', max(distances), 'Min =', min(distances)




class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)


def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())






def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    randomEvenNumber = random.randint(0,99)
    if(randomEvenNumber % 2 == 0):
        return randomEvenNumber
    else:

        return randomEvenNumber+1

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    randomEvenNumber = random.randint(10,20)
    if(randomEvenNumber % 2 == 0):
        return randomEvenNumber
    else:

        return randomEvenNumber+1


print random.randrange(0,10)


def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

# print dist1()
# print dist2()


# mylist = []

# random.seed(0)
# for i in xrange(random.randint(1, 10)):
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         mylist.append(number)
#     print mylist


# mylist = []
#
# for i in xrange(random.randint(1, 10)):
#     random.seed(0)
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         if number not in mylist:
#             mylist.append(number)
# print mylist