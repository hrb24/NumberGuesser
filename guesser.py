# Harrisons Number Guess Program
# Guesses a number between 1 and 100
# Created: 08/11/2021
# Last edit: 08/11/2021

import random
def main():
    #Initialize the program
    print("Guess a number between 1 and 100.")
    # randomNumber = 35 for debugging only
    randomNumber = random.randint(1,100)
    # print("The random number is: ", randomNumber)
    # Create a boolean variable to note if random number is guessed or not
    found = False
    
    #Run through the guessing process
    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == randomNumber:
            print("You got it!")
            found = True;
        elif userGuess >  randomNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")
        
    #Print congratulations and goodbye
    print("Thanks for playing our game!")
    
if (__name__ == "__main__"):
    main()


