# Create a random password for money import called randompass1
randompass1 = "1234"

# Import the random module
import random

# Create the user's balance
Balance = 100

# Create the users score
score = 0

# Startup the machine and give the user an introductory message
print("Welcome to Slot-Machine, increase your balance to earn more rewards:")

# Give the user the option to start up or import more balance
startup = input("To play straight away, press P. To import more balance, press I: ")

# The option where the user imports more money
if startup == "I":
    print("You have chosen to import more money to your balance.")
    upass = input("Please input the password to import... ")

    # ask the user how much they would like to import
    if upass == randompass1:
        print("You have chosen to import more money to your balance.")
        uamount = int(input("How much would you like to import? "))
        Balance = Balance + uamount
        print("Your balance is now £"  + str(Balance) + ". ")
    else:
        print("Incorrect password. Import aborted.")
else:
    print("You have chosen to play straight away.")

# Start the game and begin the loop
while True:
    
    # As the user how much they want to bet
    Amount = int(input("How much would you like to bet? "))
    
    ## If the amount bet is 0 break the loop
    if Amount < 1:
        print ("You cannot bet 0, the game will now reset")
        break
   
    # Subtract the amount the user has bet
    Balance = Balance - Amount
    
    # Randomize the wheels.
    spin1 = random.choice(["Cherry-🍒", "Orange-🍊", "Plum---🫐", "Bell---🔔", "Bar----🍫", "Seven--❼"])
    spin2 = random.choice(["Cherry-🍒", "Orange-🍊", "Plum---🫐", "Bell---🔔", "Bar----🍫", "Seven--❼"])
    spin3 = random.choice(["Cherry-🍒", "Orange-🍊", "Plum---🫐", "Bell---🔔", "Bar----🍫", "Seven--❼"])
    
    # User win scenario.
    if spin1 == spin2 == spin3:
        Balance = Balance + Amount * 2
        print (" ")
        print (spin1)
        print (spin2)
        print (spin3)
        print (" ")
        print("You won! ")
        print("Your balance is now £" + str(Balance) + "! ")
        
        # Give user a warning if their ballance falls below the recommended amount.
        if Balance < 15:
            print ("WARNING! BALANCE EXTREMELY LOW! ")
            
        # Update the score
        if Balance >= score:
            # Assign the data in the Balance variable into the score variable
            score = Balance
            # Display a message to the user saying that they have a new high score
            print ("New High Score of " + str(score) + "! ")
    
            # Open or create a file to hold the scores
            with open('scores.txt', 'a') as scores:
                scores.write(str(score) + '\n')
            
    # User lose scenario.    
    else:
        print (" ")
        print (spin1)
        print (spin2)
        print (spin3)
        print (" ")
        print ("You lost! ")
        print("Your balance is now £" + str(Balance) + "! ")
        
        # Update the score
        if Balance >= score:
            # Assign the data in the Balance variable into the score variable
            score = Balance
            # Display a message to the user saying that they have a new high score
            print ("New High Score of " + str(score) + "! ")
            
            # Open or create a file to hold the scores
            with open('scores.txt', 'a') as scores:
                scores.write(str(score) + '\n')
        
        # Give user a warning if their ballance falls below the recommended amount.
        if Balance < 15:
            print ("WARNING! BALANCE EXTREMELY LOW! ")
    
    # Restart the game if they go bankrupt.        
    if Balance < 1:
        print ("You have gone bankrupt, the game will now reset. ")
        break