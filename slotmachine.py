# Create the users balance
balance = 100

# Create the users score
score = 0

# Import the random module
import random

# Create a loop while asking the user for username
while True:
        
        # Print the user a welcome message
        print ("Welcome to Slot-Machine!")
        
        # Prompt the user to enter their username
        u_name = input ("Please enter a username. ")
        
        # Read back the name to them
        print ("Your user name will be " + u_name + ". ")
        
        # Ask the user if they are sure they would like it to be their name
        choice = input ("Are you sure you would like this to be your user name? (y, n) ")
        
        # If they are sure
        if choice == "y":
            
            # Print a message confirming thay have chosen to keep that name
            print ("Great! Your name will be " + u_name + "! ")
            
            # Break out of the loop
            break
        
        # If they are not sure
        if choice == "n":
            
            # Tell the user that they have decided to reset your username then return to the start of the loop
            print ("You have decided to reset your user name.")

# Create a loop
while True:
    
    # If the user goes bancrupt, break the loop
    if balance < 1:
        print ("you are now bancrupt! Please start again. ")
        break
    
    print ("What would you like to do? View high scores or play? (play, view) ")
    vorp = input ("Please select an option. ")
    
    if vorp == "play":
        amount = int(input("How much would you like to bet? "))
        balance = balance - amount

        # Randomise the wheels
        spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
        spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
        spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])

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
            
            # Update the score
            if balance > score:
                score = balance
                
                # print a message to the user telling them their current score
                print ("New high score of " + str(score) + "! ")
                
                # Open "scores.txt" as scores
                with open ("scores.txt", "a") as scores:
                    
                    # Write the user high score to "scores.txt" on a new line
                    scores.write (" " + u_name + " | £" + str(score) + "\n")
                    
            # Tell the user if their balance is low
                if balance <= 15:
                    print ("Balance Low! ")
                
        # User lose scenario.    
        else:
            print (" ")
            print (spin1)
            print (spin2)
            print (spin3)
            print (" ")
            print ("You lost! ")
            print("Your balance is now £" + str(balance) + "! ")
            
            # Update the score
            if balance > score:
                score = balance
                
                # print a message to the user telling them their current score
                print ("New high score of " + str(score) + "! ")
                
                # Open "scores.txt" as scores
                with open ("scores.txt", "a") as scores: # Open in append mode
                    
                    # Write the user high score to "scores.txt" on a new line
                    scores.write (" " + u_name + " | £" + str(score) + "\n")
                    
            # Tell the user if thier balance is low
            if balance <= 15:
                print ("Balance Low! ")
                    
            
    
    # Read the scores                
    elif vorp == "view":
        
        # Open "scores.txt" as scores
        with open("scores.txt", "r") as scores: # open scores in read mode
            
            # Save the contents of "scores.txt" in the variable content
            content = scores.read()
            
            # print content
            print(content)

    # Give the user a message tellign them to enter a valid input
    else:
        print ("Please enter a valid input. Please retry. ")
        
