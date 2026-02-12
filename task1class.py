import random
import os

    
class rand_num_game:
    
    # clear console and show instructions
    os.system("clear||cls")
    print("Welcome to the number guessing game!")
    print("I will pick a secret number from 1 to 100. You must guess it!")

    def generateSecret(self):
        #generates random number from 1-100
        self.number = random.randint(1,100)

    def getGuess(self):
        #get the users's guess
        while True:
            try:
                self.guess = int(input("Enter your guess. It should be an integer"))
                if 1 <= self.guess <= 100:
                    break
            except:
                pass
            print("That is not a valid input. Try again.")

    def compareGuess(self):
        #return result as 0 for equal, -1 for low, 1 for hight
        self.result = 0 if self.guess==self.number else (1 if self.guess > self.number else -1)

    def showMessage(self):
        #show message about accuracy of guess
        messages = {
            -1: "That guess is too low",
            0 : "Correct!",
            1 : "Your guess is too high"
        }
        print(messages[self.result])

    def __init__(self):
        self.generateSecret()
        numberOfGuesses = 0
        while True:
            self.getGuess()
            self.compareGuess()
            numberOfGuesses += 1
            result = self.result
            self.showMessage()
            if result == 0:
                break
        print(f"Congratulations! You guessed the secret number in {numberOfGuesses} tries")

game = rand_num_game()

while True:
    question = input("Would you like to play again? (y or n): ")
    if question == "y" or question == "Y" or question =="yes" or question == "Yes":
        rand_num_game()
    if question == "n" or question == "N" or question =="no" or question == "No":
        print("exiting game...")
        break
    else:
        print("invalid input")
    