from sys import exit 

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ") # don't do int(input("> ")) --> as int is not iterable. https://www.freecodecamp.org/news/int-object-is-not-iterable-python-error-solved/#:~:text=If%20you%20are%20running%20your,%2C%20dictionaries%2C%20and%20so%20on.
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy boi.")    


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")        
    bear_moved = False

    # for the while loop below basically the choice condition has to be met i.e. taunt bear in order to then test the booleans statement i.e. and not bear_moved etc.
    # Those are the conditions for the if statments.
    # In general if bear_moved = False the only way the if statement will run is if --> and not bear_moved is used.
    # If bear_moved = True the only way the if statement will run is if --> and bear_moved is used.
    # The and not bear_moved doesn't actually change the value of bear moved, it's just testing if its false, if it isn't then the if/elif statement can't run.
    # The and bear_moved doesn't actually change the value of bear moved, it's just testing if its true, if it isn't then the if/elif statement can't run. 

    while True: # makes an infinite loop.
        choice = input("> ")
                                     
        if choice == "take honey":          # https://stackoverflow.com/questions/26069605/learn-python-the-hard-way-exercise-35-boolean-expression
            # print(bear_moved) # bear moved is False
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved: # test succeeds as bear_moved = False so you use not to invert the test i.e. and not bear_moved.
            # print(bear_moved) # bear moved is False 
            print("The bear has moved from the door.")
            print("You can go through it now.")     
            bear_moved = True # once you type 'taunt bear' the bear_moved becomes true therefore the two elif statements below can be used.
        elif choice == "taunt bear" and bear_moved: # test succeeds as bear_moved = True so you don't need to invert the test so you would use i.e. and bear_moved.
            # print(bear_moved) # bear_moved is True  
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            # print(bear_moved) # bear moved is True 
            gold_room()
        else:
            print("I got no idea what that means.")           


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!") 
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")        

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room() 
    else:
        dead("You stumble around the room until you starve.")


start()