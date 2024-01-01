# Create the users balance
balance = 100

# Create the users score
score = 0

# Import the random module
import random

# Spin wheels function
def spin_wheels():
    spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
    spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
    spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])

# Login function    
def login():
    while True:
        print ("Welcome to Slot-Machine!")
        u_name = input ("Please enter a username. ")
        print ("Your user name will be " + u_name + ". ")
        choice = input ("Are you sure you would like this to be your user name? (y, n) ")
        if choice == "y":
            break
        if choice == "n":
            print ("You have decided to reset your user name.")

# Enter bet function           
def bet():
    amount = int(input("How much would you like to bet? "))
    balance = balance - amount

# Function to justify user win
def user_win():
    if spin1 == spin2 == spin3:
        balance = balance + amount * 2
        print (" ")
        print (spin1)
        print (spin2)
        print (spin3)
        print (" ")
        print ("You win your balance is now £" + balance + "! ")

def user_lose():
    

# Update score function   
def update_score():
    if balance > score:
        with open ("scores.txt", "a") as scores:
            scores.write (" " + u_name + " | " + str(score) + "\n")
            

            


            

        
        
