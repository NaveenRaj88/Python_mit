__author__ = 'anandran'

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, intSet2):
        """ Returns the intersection of the 2 sets """
        intersectSet=intSet()
        for e in self.vals:
            if e in intSet2.vals:
                intersectSet.insert(e)
        return intersectSet

    def __len__(self):
        return len(self.vals)

    def len(self):
        return len(self.vals)

s1 = intSet()
s1 = Ellipsis
print s1

setA= [-19,-16,-13,-12,-10,-9,3,7,8,14]
setB= [-20,-19,-6,-1,0,3,8,11,16,19]
set1 = intSet()
set2 = intSet()
for a in setA:
    set1.insert(a)
for b in setB:
    set2.insert(b)
print set1.intersect(set2)

print len(set1)
