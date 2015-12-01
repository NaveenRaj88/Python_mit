__author__ = 'anandran'

s = 'azcbobobegghakl'
def countVowels(string):
    count=0;
    l=list(string)
    for i in l:
        if i in 'aeiou':
            count=count+1
    print 'Number of vowels: '+str(count)


countVowels(s)