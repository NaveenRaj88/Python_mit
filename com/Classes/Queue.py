__author__ = 'anandran'

class Queue():

    def __init__(self):
        self.vals=[]

    def insert(self, value):
        self.vals.append(value)

    def remove(self):
        if len(self.vals) == 0:
            raise ValueError('No elements in the Queue')
        value = self.vals[0]
        self.vals.remove(value)
        return value


q = Queue()
# q.remove()
#
# list=[1,2,3,4]
# print list.append(5)
# print list
# print list[0]
# list.remove(0)
# print list



class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print self.incantation


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())


