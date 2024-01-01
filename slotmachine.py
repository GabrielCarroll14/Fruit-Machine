# Create the users balance
balance = 100

# Create the users score
score = 0

# Import the random module
import random

# Start of game setup

# Run the login function
while True:
        print ("Welcome to Slot-Machine!")
        u_name = input ("Please enter a username. ")
        print ("Your user name will be " + u_name + ". ")
        choice = input ("Are you sure you would like this to be your user name? (y, n) ")
        if choice == "y":
            print ("Great! Your name will be " + u_name + "! ")
            break
        if choice == "n":
            print ("You have decided to reset your user name.")

while True:
    print ("What would you like to do? View high scores or play? (play, view) ")
    vorp = input ("Please select an option. ")
    
    if vorp == "play":
        amount = int(input("How much would you like to bet? "))
        balance = balance - amount

        spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
        spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])
        spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven  ❼"])

        # User win scenario.
        if spin1 == spin2 == spin3:
            balance = balance + amount * 2
            print (" ")
            print (spin1)
            print (spin2)
            print (spin3)
            print (" ")
            print("You won! ")
            print ("Your balance is now £" + str(balance) + "! ")
            if balance > score:
                print ("New high score of " + str(score) + "! ")
                score = balance
                with open ("scores.txt", "a") as scores:
                    scores.write (" " + u_name + " | £" + str(score) + "\n")
                
        # User lose scenario.    
        else:
            print (" ")
            print (spin1)
            print (spin2)
            print (spin3)
            print (" ")
            print ("You lost! ")
            print("Your balance is now £" + str(balance) + "! ")
            if balance > score:
                print ("New high score of " + str(score) + "! ")
                score = balance
                with open ("scores.txt", "a") as scores:
                    scores.write (" " + u_name + " | £" + str(score) + "\n")
                    
    elif vorp == "view":
        with open("scores.txt", "r") as scores:
            content = scores.read()
            print(content)

        
        
        


            

            


            

        
        
