# Harrisons Number Guess Program
# Guesses a number between 1 and 100
# Created: 08/11/2021
# Last edit: 08/11/2021

import random
def main():
    #Initialize the program
    print("Welcome to the Random Number Guesser!")
    print("Between which two values do you want to guess?")
    print("Lower bound: ")
    lowerBound = int(input())
    print("Upper bound: ")
    upperBound = int(input())
    
    # Output the value range for the user
    print("You will be guessing between ", lowerBound, " and ", upperBound)
    
    # Call function randomNumber using upper and lower bound parameters
    # Assign the return value to randInt
    randInt = randomNumber(lowerBound, upperBound)
    
    # Call Guesser function to loop through guessing process
    guesser(randInt)
    
    #Print congratulations and goodbye
    print("Thanks for playing our game!")
    
    
def randomNumber(lower, upper):
    randomNumber = random.randint(lower,upper)
    return randomNumber
    
def guesser(randomNumber):
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
    
if (__name__ == "__main__"):
    main()

