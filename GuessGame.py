#A Guessing Game
import random
SecretNumber = random.randint(1, 11)
print (SecretNumber)
Guess = int(input("Guess a number between 1 and 10: "))
if Guess > SecretNumber:
    print("too high")
elif Guess < SecretNumber:
    print("too low")
else:
    print("Correct")