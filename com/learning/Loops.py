__author__ = 'anandran'
import string

text = 'Koala bears are soft and cuddly'
for i in range(0,len(text)):
    nonPunctuatedText = ''
    if text[i] in string.punctuation:
        nonPunctuatedText[i]=" "
    else:
        nonPunctuatedText[i]=text[i]
print(nonPunctuatedText)