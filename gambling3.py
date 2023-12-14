import time
import random

balance = 0

def intro():
    global balance
    answer = input("""Type "work" to work, "gamble" to gamble, or "exit" to exit
    (you cannot gamble if balance is 0, check balance with "balance"): """)

    if answer.upper() == "BALANCE":
        print("Your balance is: $", balance)
        time.sleep (1)
        intro()
    elif answer.upper() == "WORK":
        work()
    elif answer.upper() == "GAMBLE":
        gamble()
    elif answer.upper() == "EXIT":
        EXIT()
    else:
        intro()

def lose(WagerAmount):
    global balance
    balance -= WagerAmount

def win(WagerAmount):
    global balance
    balance += WagerAmount

def wager():
    global balance
    global WagerAmount
    WagerAmount = int(input("Wager: "))
    if WagerAmount <= balance:
        return True
    else:
        print("Insufficient Funds")
        return False

def work():
    global balance
    print("Working, wait 10 seconds....")
    time.sleep(10)
    print("You have completed your shift, 10 dollars have been added to your balance")
    balance += 10
    intro()

def gamble():
    global balance
    if balance > 0:
        gambling = input("""Welcome to gambling, type "Guessing" to start a guessing game, or "exit" to exit: """)
        if gambling.upper() == "GUESSING":
            GuessingGame()
        elif gambling.upper() == "EXIT":
            intro()
    else:
        print("Insufficient funds to gamble with")
        time.sleep (0.7)
        intro()

def GuessingGame():
    global balance
    if wager():
        number = random.randint(1, 10)
        
        print("Welcome to the guessing game! You have 3 guesses, guess a number between 1 and 10.")

        guesses = 0
        while guesses < 3:
                guess = int(input("Guess: "))
                if guess == number:
                    print("Congrats, you have guessed the number!")
                    win(WagerAmount)
                    intro()
                else:
                    print("Sorry, that is not the number")
                    guesses += 1
                    if guess > number:
                        print("Your guess is too high, try again!")
                    else:
                        print("Your guess is too low, try again!")
        else:
                print("Sorry, you have run out of guesses")
                print("The number was", number)
                lose(WagerAmount)
                intro()
    else:
        intro()

def EXIT():
    print("Exiting... ")
    time.sleep(2)
    exit()

intro()