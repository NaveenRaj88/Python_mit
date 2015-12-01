__author__ = 'anandran'

from ps3b import SimpleVirus, Patient
import random

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

# Enter your definitions for the ResistantVirus and TreatedPatient classes in this box.
class ResistantVirus1(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.mutProb = mutProb
        self.resistances = resistances

    def isResistantTo(self, drug):
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        if (all(self.isResistantTo(d) for d in activeDrugs) and
            random.random() <= self.getMaxBirthProb() * (1 - popDensity)):
            resistances = {k:v if random.random() > self.mutProb else not v
                           for k, v in self.resistances.items()}
            return ResistantVirus1(self.getMaxBirthProb(), self.getClearProb(),
                                  resistances, self.mutProb)
        raise NoChildException


# Problem 4: b) TreatedPatient
class TreatedPatient1(Patient):

    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.drugs =[]

    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        return self.drugs

    def getResistPop(self, drugResist):
        return len([v for v in self.viruses if all(v.isResistantTo(d)
                                                   for d in drugResist)])

    def update(self):
        self.viruses = [v for v in self.viruses if not v.doesClear()]
        popDensity = len(self.viruses) / float(self.maxPop)
        for v in self.viruses[:]:
            try:
                self.viruses.append(v.reproduce(popDensity,
                                                self.getPrescriptions()))
            except NoChildException:
                pass
        return len(self.viruses)


virus = ResistantVirus1(1.0, 0.0, {}, 0.0)
patient = TreatedPatient1([virus], 100)
for i in range(100):
    patient.update()
print patient.update()