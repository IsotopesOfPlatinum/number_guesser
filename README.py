low = 0
high = 100
guess = (high + low)/2
x = 'h'
print 'Please think of a number between 0 and 100!'

while x != 'c':
    print 'Is your secret number ' + str(guess) + '?'
    print "Enter 'h' to indicate the guess is too high.",
    print "Enter 'l' to indicate the guess is too low.", 
    print "Enter 'c' to indicate I guessed correctly.",
    x = raw_input()
    
    if str(x) == 'h':
        high = guess
    elif str(x) == 'l':
        low = guess
    elif str(x) == 'c':
        print "Game over. Your secret number was: " + str(guess)
    else:
        print 'Sorry, I did not understand your input.'
    guess = (high + low)/2
