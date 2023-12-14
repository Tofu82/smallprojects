#Simple Shop (with only 1 of each item)
import time

shop_inventory = ["BOOTS","HAT","JACKET"]

#Buying an item (used for #buy2)
def buy():
    shop_inventory.remove (answer_2.upper())

#Exiting the store
def exit_store():
    print ("Shopkeeper: Goodbye!")
    time.sleep (2)
    print ("*You exit the store*")

#Actually buying an item
def buy2():

        while len(shop_inventory) > 0:
            print("Shopkeeper: Here is our inventory:")
            print (shop_inventory)
            time.sleep(1)
            global answer_2
            answer_2 = input("""
Type "Exit" to leave the store
Type the name of an item to buy it
:""")


            if answer_2.upper() == "BOOTS":
                buy()
                print ("You have succesfully bought Boots")
                time.sleep(1)
            elif answer_2.upper() == ("HAT"):
             buy()
             print ("You have succesfully bought a Hat")
             time.sleep(1)
            elif answer_2.upper() == "JACKET":
             buy()
             print ("You have succesfully bought a Jacket")
             time.sleep(1)
            elif answer_2.upper() == "EXIT":
             exit_store()
        else:
            time.sleep(0.5)
            print ("Shopkeeper: Sorry, we are out of stock!")
            time.sleep (0.5)
            print ("*You exit the store*")


#Greeting
print("Shopkeeper: Hi and welcome to the shop!")
time.sleep(2)
print ("Shopkeeper: Would you like to buy something?")
time.sleep(2)

answer = str(input("""What would you like to do?
Type "Buy" to buy something
Type "Exit" to exit the store
:"""))
if answer.upper() == "BUY":
    buy2()
elif answer.upper() == "EXIT":
    exit_store()