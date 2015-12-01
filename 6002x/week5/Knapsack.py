__author__ = 'anandran'

class Item:
    def __init__(self, name, value, weight):
        self.name=name
        self.value=value
        self.weight=weight

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    return Items

def greedy(Items, maxWeight, keyFcn):
    assert type(Items) == list and maxWeight >= 0
    ItemsCopy = sorted(Items,key=keyFcn, reverse=True)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight < maxWeight and i < len(Items):
        if(totalWeight+ItemsCopy[i].getWeight() <= maxWeight):
            result.append(ItemsCopy[i])
            totalWeight = totalWeight+ItemsCopy[i].getWeight()
            totalVal+=ItemsCopy[i].getValue()
        i+=1
    return (result,totalVal)

