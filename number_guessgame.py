# A simple number guessing game
import random
def guessgame():
    """ A simple number guessing game """
    number = random.randint(0 , 100)    # This will assign a random integer value to variable "number"
    print("You have 5 chances only.")
    chance = 0
    while(chance < 5):
        i = int(input("Guess the number (the number is bertween 0 - 100):"))
        if i < number:
            print("Entered number is less, increase it")
            chance=chance+1
            print("Number of attempts left are ", 5-chance)
            continue
        elif i > number:
            print("Entered number is greater, decrease it")
            chance=chance+1
            print("Number of attempts left are ", 5-chance)
            continue
        elif i == number:
            print("Congratulations! you've guessed the number correctly.")
            chance=chance+1
            break
    if(chance==5):
        print("Game Over.")
        print(f"The number was {number} " )

if __name__ == '__main__':
    print(" ~~~~~~~~~~~The Number Guessing Game!~~~~~~~~~~~~~~")
    start = input("To start the game press the 's' key. ")
    if start == "s":
        guessgame()
    print("Do you want to play the game again?")
    start = input("Press 's' to play again and to quit press 'q'")
    if start == "s":
        guessgame()
    elif start == "q":
        exit()
    
