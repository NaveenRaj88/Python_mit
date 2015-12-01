__author__ = 'anandran'

start=0
end = 100
print "Please think of a number between %d and %d!" %(start,end)
continueGuessing = True
while(continueGuessing):
    guess = (end+start)/2
    print "Is your secret number %d?" %guess
    char = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if char == "c" :
        print "Game over. Your secret number was:",guess
        break
    elif char == "h" :
        end = guess
    elif char == "l" :
        start=guess
    else:
        print "wrong entry please try again"
        continue
    if start-end == 0 :
        print "you did not guess any number exiting"
        break

