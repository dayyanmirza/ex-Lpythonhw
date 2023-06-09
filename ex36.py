from sys import argv, exit

script, game = argv

print("This game is inspired by learn python3 the hardway:", script)
print(f"Welcome to {game} - adventure game based in the desert.\n")

# create the ending function
def ending():
    print("You go back to their tent and you see a pile of gold there.")
    print("You could either (please input a number): 1) take the 5kg of gold, 2) leave it. ")
 
    choice = int(input("> ")) 
    
    if choice == 1:
        die("You don't learn your lesson do you. You get killed by the chief who always checks his stash.")
    elif choice == 2:
        print("You end up staying there ") 
        print("You find a nice girl you like. The locals like you too and then you just stay for 20 years get married to the girl have kids.") 
        print("After staying for 20 years they decide to return you back home.\n")
        print("But then you confess that you lied this whole time. The chief gets angry and asks his guards to imprison you.\n")
        print("You stay in the cell for a while and die of old age...\n")
        print("For some reason though you wake up and feel as if nothing has changed cause guess what...you're still in the desert. It was all a dream!")
        start()
    else:
        print("Sorry, that's not an option.")   

# create the village function
def village():
    print("You are able to keep yourself hydrated and healthy with the remaining supplies.")
    print("You stumble upon a village but your boat is stuck a bit too far outshore on a rock.")
    print("You have two options (please input a number): 1) swim to the beach, 2) use your airhorn.")

    choice = int(input("> "))

    if choice == 1:
        die("You don't learn your lesson do you. You drown.")
    elif choice == 2:
        print("People come to see what happened") 
        print("You pretend to act like a local.")
        print("They investigate and take you in.") 
        ending() 
    else:
        print("Sorry, that's not an option.")    
 

# create boat function
def boat():
    print("You reach the boat and it has supplies but it's too heavy to keep them all.")
    print("You have to get rid of one of the three options (please input a number): 1)airhorn, 2)water bottle, 3)lighter.")

    choice = int(input("> "))

    if choice == 1:
        die("You reach a village but your boat get stuck and you have no way of contacting locals so are left stranded and die.")
    elif choice == 2:
        die("Without the water bottle you die of dehydration.")
    elif choice == 3:
        print("Good choice.")
        village()     
    else:
        print("Sorry, that's not an option.")    


# create the river function
def river():
    print("You see a boat in the middle of a river.")
    print("You have one of three options (please input a number): 1)swim to boat, 2)use the camel to swim, 3)walk around the river.")

    choice = int(input("> "))

    if choice == 1:
        die("Unfortunately you drown.")
    elif choice == 2:
        print("Good choice.")
        boat()
    elif choice == 3:
        die("You starve and die.")     
    else:
        print("Sorry, that's not an option.")     

# create the backdoor function for the red_door room.
def backdoor():
    print("You find a camel outside.")
    print("You have three options (please input a number): 1)stroke, 2)ride, 3)taunt.")

    choice = int(input("> "))

    if choice == 1:
        print("The camel becomes friendly with you and you ride it.")
        river()
    elif choice == 2:
        die("The camel starts moving vigorously to make you fall of and you land on your head.")
    elif choice == 3:
        die("He kicks you and you die.")     
    else:
        print("Sorry, that's not an option.")     


# create the red door.
def red_door():
    print("You see a red door.")
    print("You have two options: enter, walk back.")
    print("Which one do you choose?")
    door_open = False

    while True: # makes an infinite loop.
        choice = input("> ")

        if choice == 'walk back':
            start()
        elif choice == 'enter' and not door_open:
            print("You enter the door and see a cactus in the middle of the room.")
            print("Do you cut it, or leave it.")
            door_open = True 
        elif choice == 'leave it' and door_open:
            die("You die of dehydration.")
        elif choice == 'cut it' and door_open:
            print("You start drinking water from the cactus and feel better.")
            print("While drinking you walk outside through a backdoor.")  
            backdoor()     
        else:
            print("Sorry, that's not an option.")  


# create the blue door.
def blue_door():
    print("You see a blue door.")
    print("You have two options: enter, walk back.")
    print("Which one do you choose?")
    door_open = False

    while True: # makes an infinite loop.
        choice = input("> ")

        if choice == 'walk back':
            start()
        elif choice == 'enter' and not door_open:
            print("You enter the door and see food on the ground.")
            print("Do you eat, or leave it.")
            door_open = True 
        elif choice == 'eat' and door_open:
            die("You get ill and die.")
        elif choice == 'leave it' and door_open:
            print("You decide to leave it and go back. Try a different door this time.")
            start()        
        else:
            print("Sorry, that's not an option.")    
      
           

# create the die function.
def die(reason):
    print(reason, "Game over!")
    exit(0)


# First create the start position of the game. 
def start():
    print("\nYou wake up from a slumber and realise your in the desert.")
    print("There's two foot prints in front of you, one to your left and one to your right")
    print("Which one do you choose, left or right?")

    choice = input("> ")

    if choice == 'left':
        blue_door()
    elif choice == 'right':
        red_door()
    else:
        die("You die from dehydration.")

start()