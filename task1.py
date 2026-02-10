import random
import os

    
def showTitle():
    # clear console and show instructions
    os.system("clear||cls")
    print("Welcome to the number guessing game!")
    print("I will pick a secret number from 1 to 100. You must guess it!")

def generateSecret():
    #generates random number from 1-100
    return random.randint(1,100)

def getGuess():
    #get the users's guess
    while True:
        try:
            guess = int(input("Enter your guess. It should be an integer"))
            if 1 <= guess <= 100:
                break
        except:
            pass
        print("That is not a valid input. Try again.")
    return guess

def compareGuess(a,b):
    #return result as 0 for equal, -1 for low, 1 for hight
    return 0 if a==b else (1 if a > b else -1)
    # If you can't make sense of line 28, you can do the following code instead
    if a == b:
        return 0
    elif a > b:
        return 1
    elif a < b:
        return -1

def showMessage(result):
    #show message about accuracy of guess
    messages = {
        -1: "That guess is too low",
        0 : "Correct!",
        1 : "Your guess is too high"
    }
    print(result)

if __name__ == "__main__":
    showTitle()
    secretNumber = generateSecret()
    numberOfGuesses = 0
    while True:
        guess = getGuess()
        numberOfGuesses += 1
        result = compareGuess(guess,secretNumber)
        showMessage(result)
        if result == 0:
            break
    print(f"Congratulations! You guessed the secret number in {numberOfGuesses} tries")