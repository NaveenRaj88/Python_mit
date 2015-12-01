__author__ = 'anandran'

s = 'azcbobobegghakl'
z=0
index=0
while index >=0:
    index= s.find('bob', index, len(s))
    if(index <0):
        print 'Number of times bob occurs is: '+str(z)
        break
    index=index+1
    z=z+1

