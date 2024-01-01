# Create the users balance
balance = 100

# Create the users score
score = 100

# Import the random module
import random

def spin_wheels():
    spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
    spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
    spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
    
def login():
    while True:
        print ("Welcome to Slot-Machine!")
        u_name = input ("Please enter a username. ")
        print ("Your user name will be " + u_name + ". ")
        choice = input ("Are you sure you would like this to be your user name? (y, n) ")
        if choice == "y":
            break
        if choice == "n":
            print ("You have decided to reset your user_name.")