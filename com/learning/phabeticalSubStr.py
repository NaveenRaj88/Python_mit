__author__ = 'anandran'

s = 'azcbobobegghakl'
#s='abcbcd'
#s = 'abcdefghijklmnopqrstuvwxyz'
index=0
alporderlow=0
alporderend=0;
count=0
length = len(s)
while index < length:
    counter=0
    prevord=ord(s[index])
    for i in s[index+1:length]:
        curord=ord(i)
        if(curord>=prevord):
            counter=counter+1
            prevord=curord
            continue
        break
    if(counter > count):
        count=counter
        alporderlow=index
        alporderend=alporderlow+counter
    index=index+1
print 'Longest substring in alphabetical order is: '+s[alporderlow:alporderend+1]