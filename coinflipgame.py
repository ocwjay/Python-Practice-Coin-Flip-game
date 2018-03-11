# coin flip game

# gotta be able to use random module
import random

# create list as global variable
coinSide = ["heads", "tails"]
#score globals
scoreHeads = 0
scoreTails = 0

#define the game function
def gameTime():
    #request input for flip and assign to variable
    flipQ = input("Would you like to flip a coin? y/n \n")
    #checking to see what the input was
    if flipQ == "y":
        #bring global list in
        global coinSide
        #get the random index and assign to variable
        randIndex = random.choice(coinSide)
        print("It's " + randIndex + "!")
        #now to add side selection scores
        if randIndex == "heads":
            #bringing in global variable
            global scoreHeads
            scoreHeads += 1
        else:
            #global variable
            global scoreTails
            scoreTails += 1
        #printing scores
        print("Heads score:")
        print(scoreHeads)
        print("Tails score:")
        print(scoreTails)
        #restarting game
        gameTime()
    elif flipQ == "n":
        print("Another time, then.")
        gameTime()
    else:
        print("That is not a valid input. Please try again.")
        gameTime()
    
gameTime()
