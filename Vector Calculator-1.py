import time

print("Welcome to the Vector Calculator")

time.sleep(1)  # Wait for 1 seconds

print("Will this operation be addition or multiplication?")

time.sleep(1)  # Wait for 1 seconds

calc = input("Enter [A] for addition or [M] for multiplication: ")
while calc != "A" or "M":


        if calc=="A":
            print("You have chosen Addition")
            break


        if calc=="M":
            print("You have chosen Multiplication")
            break


        if not calc=="A" or calc=="M":
            calc = input("Please enter a valid command, either [A] for addition or [M] for multiplication: ")
    
