'''
PROJECT 2 --> " The Perfect Guess "

'''

import random
n = int(input("Enter a number : "))
while (n<1):
    print("Number should be greater than 1")
    n = int(input("Enter a number : "))
computer = random.randint(1,n)
guess = -1
guesses = 0
while (computer != guess ):
    guess = int(input("Guess a random Number : "))

    guesses = guesses+1
    if (guess>computer):
        print("Lower number plz")
    elif(guess<computer):
        print("Higher number plz")
    
print(f"It took {guesses} guesses for you to guess it right ")