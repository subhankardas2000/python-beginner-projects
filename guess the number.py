import random #importing random module to genertae random int value
n = 20 #random genertaed value will be between 0-20
to_be_guessed=int (n *random.random()) + 1 #generating random value and stored in the variable

guess = 0#initializing the guess number to 0
for i in range(10):#number of tries a user can make
    while guess != to_be_guessed:#condition for while loop

        guess = int (input("New number: "))#taking the input of the number that u have guessed

        if guess > 0:
            if guess>to_be_guessed:
                print("Number too large")

            elif guess<to_be_guessed:
                print("Number too small")
        else:
            print("Sorry that you're giving up!")
        break

    else:
        print("Congratulation. You made it!")#if you have guessed right then this else will be executed