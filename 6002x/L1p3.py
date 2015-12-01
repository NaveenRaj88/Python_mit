__author__ = 'anandran'

f = open('julyTemps.txt')

def getHighAndLowTempTuples():
    highTempList=[]
    lowTempsList=[]
    while True:
        s = f.readline()
        if(s == ''):
            break
        fields = s.split()
        if (len(fields)==3 and fields[0].isdigit()):
            highTempList.append(int(fields[1].strip()))
            lowTempsList.append(int(fields[2].strip()))
    print highTempList,lowTempsList

getHighAndLowTempTuples()