import random
import time
#Guessing Game
number = random.randint(1,10)

#Intro
print ("Welcome to the guessing game!")
time.sleep(1)
print ("I am thinking of a number between 1 and 10")
time.sleep(1)
print ("You have 3 guesses")

#Checking Guess

guesses = 0
while guesses < 3:
  guess = int(input("Guess: "))
  if guess == number:
    print("Congrats you have guessed the number!")
    break
  elif guess != number:
    print("Sorry that is not the number")
    guesses = guesses + 1
  
  if guess > number:
    print ("Your guess is too high, try again!")
  elif guess < number:
    print ("Your guess is too low, try again!")
else:
  print("Sorry you have run out of guesses")
  print("The number was", number)