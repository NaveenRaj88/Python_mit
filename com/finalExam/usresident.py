## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
from string import lowercase


class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        if status.lower() not in ['citizen','legal_resident', 'illegal_resident' ]:
            raise ValueError
        super(USResident,self).__init__(name)
        self.stats=status
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.stats

a = USResident('Tim Beaver', 'citizen')
print a.getStatus()
print a.getLastName()
# b = USResident('Tim Horton', 'non-resident')


class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    frob = atMe
    location = 0
    endAddition = False
    while True:
        if newFrob.myName() > frob.myName() and location >= 0:
            location = location+1
            if(frob.getAfter() == None):
                endAddition = True
                break
            frob=frob.getAfter()
        elif newFrob.myName() < frob.myName() and location <= 0:
            location = location-1
            if(frob.getBefore() == None):
                endAddition = True
                break
            frob = frob.getBefore()
        else:
            if(not endAddition):
                if(location >0 ):
                   frob = frob.getBefore()
                elif location < 0:
                    frob = frob.getAfter()
            break
        if frob == None:
            break
    if location <=0:
        prevFrob = frob.getBefore()
        frob.setBefore(newFrob)
        newFrob.setAfter(frob)
        if prevFrob != None:
            prevFrob.setAfter(newFrob)
            newFrob.setBefore(prevFrob)
    elif location > 0:
        nextFrob = frob.getAfter();
        frob.setAfter(newFrob)
        newFrob.setBefore(frob)
        if(nextFrob != None):
            newFrob.setAfter(nextFrob)
            nextFrob.setBefore(newFrob)

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

# frob = andrew
# while True:
#     if(frob == None):
#         break
#     print frob.myName()
#     frob = frob.getAfter()
#
# print 'in reverse'
# frob = ruth
# while True:
#     if(frob == None):
#         break
#     print frob.myName()
#     frob = frob.getBefore()

insert(Frob("alvin"), Frob("alvin"))

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if(start.getBefore() ==None):
        return start
    else: return findFront(start.getBefore())

print findFront(martha).myName()