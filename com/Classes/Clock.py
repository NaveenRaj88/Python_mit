__author__ = 'anandran'

class Clock(object):
    def __init__(self, time):
	    self.time = time
    def print_time(self):
	    time = '6:30'
	    print self.time

clock = Clock('5:30')
clock.print_time()


class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print time

clock = Clock('5:30')
clock.print_time('10:30')



class Clock(object):
    def __init__(self, time):
	    self.time = time
    def print_time(self):
	    print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()





class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8

# w1 = Weird(X, Y)
# print w1.getX()


w4 = Wild(X, 18)
print w4.getX()




class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Coordinate('+str(self.getX())+','+str(self.getY())+')'

c=Coordinate(7,9);

print c

print repr(c)