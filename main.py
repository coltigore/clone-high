yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("*You awaken in a high school Boy's room. Standing before you is the 16 year-old clone of JFK* Err ehh, just who are you, chowdah head?\n")
print("" + name + ", Eh? Welcome to Clone High!")
print("*JFK Punches you in the gut and walks out of the bathroom laughing*\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step out of the bathroom?\nyes/no\n")
    if response == "yes":
        print("You head out into the hallway.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see Cleopatra and Abraham Lincoln talking with one another.")
    print("To your right, you se Ghandi, staring at a mural of himself in the nude by Vincent Van Gogh.")
    print("There is a wall of lockers in front of you.")
    print("Behind you is door to the bathroom.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
