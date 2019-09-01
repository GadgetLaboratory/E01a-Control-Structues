#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
#The script is saying hi to you!  How nice.
colors = ['red','orange','yellow','green','blue','violet','purple']
#This is setting an array of colors for the game to choose from.
play_again = ''
#This is setting an empty string variable to adjust later.
best_count = sys.maxsize            # the biggest number
#This logs the number of tries it took to get the correct answer after completing a round.
while (play_again != 'n' and play_again != 'no'):
    #This makes sure you want to play again; if not, it'll exit the loop.
    match_color = random.choice(colors)
    #This decides a random color from the given array up above.
    count = 0
    #Sets the amount of tries you're currently on.
    color = ''
    #Sets an empty string to later take the color value that you input.
    while (color != match_color):
        #If you haven't gotten the right answer yet, this will take you in for another try.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #The main question, which asks you what your favorite color is.
        color = color.lower().strip()
        #This takes the string you put into the question and strips it of all spaces and makes it lowercase.
        #If you put symbols into the response, it won't catch it even if it's right, so basically don't do that.
        count += 1
        #This ticks the "color" variable up 1 value with your response.
        if (color == match_color):
            #This checks to see if you guessed the correct color.
            print('Correct!')
            #If you have, then you're rewarded with this, and you'll be taken out of this while loop. 
        else:
            #If you didn't:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
            #It will direct you to try again and then start the while loop over, rubbing in how many times you've failed this completely random activity.
    print('\nYou guessed it in {0} tries!'.format(count))
    #This prints how many tries it took you -- the ultimate value of the "count" variable.
    if (count < best_count):
        #This checks to see if the amount of times it took you this attempt was better than your best before.
        print('This was your best guess so far!')
        #If it was, it rewards you with this,
        best_count = count
        #and the "best_count" variable is updated to reflect it.
    play_again = input("\nWould you like to play again? ").lower().strip()
    #This stores the variable that this while loop checks, and confirms if it isn't, in some way shape or form, "no".
print('Thanks for playing!')
#And if you don't want to play any more, the script tells you good-bye.  What a nice computer program.