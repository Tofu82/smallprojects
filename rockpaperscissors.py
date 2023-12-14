
#Rock, Paper, Scissors
import time
import random

#Opponent AI
def ai():
  choice = int(random.randrange(1,3))
  if choice == 1:
    return "rock"
  elif choice == 2:
    return "paper"
  elif choice == 3:
    return "scissors"

#Game Mechanics 
def game():
  Game_Done = False

  while Game_Done is False:
    player = input("Choose either rock, paper or scissors:")

    if player.lower() == "rock" and ai() == "rock":
      print ("You both chose rock, it's a tie!")
      print ("Try again:")
    elif player.lower() == "rock" and ai() == "paper":
      print ("You chose rock, the computer chose paper, you lose!")
      Game_Done = True
    elif player.lower() == "rock" and ai() == "scissors":
      print ("You chose rock, the computer chose scissors, you win!")
      Game_Done = True
    elif player.lower() == "paper" and ai() == "rock":
      print("You chose paper, the computer chose rock, you win!")
      Game_Done = True
    elif player.lower() == "paper" and ai() == "paper":
      print ("You chose paper, the computer chose paper, it's a tie!")
      print ("Try again:")
    elif player.lower() == "paper" and ai() == "scissors":
      print("You chose paper, the computer chose scissors, you lose!")
      Game_Done = True
    elif player.lower() == "scissors" and ai() == "rock":
      print("You chose scissors, the computer chose rock, you lose!")
      Game_Done = True
    elif player.lower() == "scissors" and ai() == "paper":
      print("You chose scissors, the computer chose paper, you win!")
      Game_Done = True
    elif player.lower() == "scissors" and ai() == "scissors":
      print("You chose scissors, the computer chose scissors, it's a tie!")
      print ("Try again:")


#Introduction
print ("Welcome to Rock, Paper, Scissors!")
time.sleep (0.5)
answer = input('''Type "Play" to start the game"
> ''')

#Start Game
answered = False
while answered is False:
  if answer.upper() == "PLAY":
    answered = True
    print ("Okay, let's play")
    game()
  else:
   print("Sorry, I didn't understand that, please try again(check the capiatalization)")
   break