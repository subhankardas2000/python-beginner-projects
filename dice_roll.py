#How it works
#This is a classic “roll the dice” program.
#We will be using the random module for this,since we want to randomize the numberswe get from the dice.

#We set two variables (min and max) , lowest and highest number of the dice.
#We then use a while loop, so that the user can roll the dice again.

#The roll_again can be set to any value, but here it’s set to “yes” or “y”,
#but you can also add other variations to it.

#Rolling the dice

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again =input("Roll the dices again?  : ")