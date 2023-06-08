from sys import argv, exit

script, game = argv

print("This game is inspired by learn python3 the hardway:", script)
print(f"Welcome to {game} - adventure game based in the desert.\n")

# create the ending function


# create the village function


# create the boat function


# create the river function
#def river:

# create the backdoor function for the red_door room.
def backdoor():
    print("You find a camel outside.")
    print("You have three options: 1)stroke, 2)ride, 3)taunt.")

    choice = int(input("> "))

    if choice == 1:
        print("The camel becomes friendly with you and you ride it.")
        #river()
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
            print("While drinking you walk outside outside through a backdoor.")  
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