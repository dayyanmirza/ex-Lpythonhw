# “Gothons from Planet Percal #25”

"""
Notes:

I think what I do is create the classes and then when I'm making the test to run it then I can use the various classes to make objects and use its attributes.

"""

# My Solution 
from sys import exit 

# Scene is the parent class for the scenes.
class Scene(object): # For a scene we have description (print), then the engine tells you the next room. How do we go to the next room?, SCENE -> ENGINE -> next_scene 
    
    def enter(self, scene):
        self.scene = scene  # The way I coded it I dont even need to use the Scene class.


class Engine(object): 

    def __init__(self, scene_map): 
        self.scene_map = scene_map # attribute scene_map

    def play(self): 
        print('---' * 45,'\n')
        # Use self.scene_map.next_scene to get the instance of the next scene
        current_scene = self.scene_map.next_scene(self.scene_map.start_scene)
        current_scene.enter()  # Call the enter method of the current scene
                

# class Death(Scene): # Don't know how to incorporate this into my code. Whether I should explicitly mention in the text.

#     def enter(self):
#         print("You get gobbled up by a Gothon behind you.")
        

class CentralCorridor(Scene): # 1st scene  

    def enter(self):
        print("You are at the central corridor.")
        print("A Gothon appears to be there.")
        print("You have two options 1) Attack the Gothon, 2) Say 'you look good today.' ")
        choice = int(input("> "))       

        if choice == 1:
            print("You get eaten by the Gothon.")
            exit(0)
        elif choice == 2:
            print("You successfully pass the corridor while the Gothon is smiling and laughing uncontrollably.")  
        else:
            print("That's not a number.")
            exit(0)

class LaserWeaponArmory(Scene): # 2nd scene 

    def enter(self):
        print("You enter the laser weapon armory.")
        print("There is a bomb contained inside a glass.")
        print("There's a keypad next to the glass, where you can enter numbers.")
        print("But there's two no.'s on the glass that you could write, 1) 123, 2) 098 --> Which one do you chose?")
        choice = int(input("> "))        

        if choice == 1:
            print("It's not that easy, the bomb explodes.")
            print("Game over.")
            exit(0)
        elif choice == 2:
            print("Correct.") 
            print("The glass opens up.")
            print("You grab the bomb and put it in your bag." )
        else:
            print("That's not a number.")
            exit(0)

class TheBridge(Scene): # 3rd scene 

    def enter(self):
        print("You see a bridge.")
        print("The bridge has a gothon on it.")
        print("You can either 1) throw the bomb at the Gothon  2) Try to run around the Gothon.")  
        choice = int(input("> "))        

        if choice == 1:
            print("The gothon explodes into a million pieces.")
            print("There's now a hole in the bridge.")
            print("You decide to jump over it, and you survive.")
        elif choice == 2:
            print("Well that was a bad idea.")
            print("You get swallowed by the Gothon.")  
            exit(0)
        else:
            print("That's not a number.")
            exit(0)

class EscpaePod(Scene): # 4th scene 

    def enter(self):
        print("There are three escape pods in front of you.")
        print("Which one do you choose?")
        print("Do you pick 1, 2, or 3.") 
        choice = int(input("> "))        

        if choice == 1:
            print("Wrong answer. The espace pod explodes with you inside it.")
            print("Hint: 1st the worst, 2nd the best, 3rd the one with the hairy chest.")   
            exit(0)
        elif choice == 2:
            print("Yesssss!")
            print("You are able to escape to a planet below.")
            print("You Win.")  
            exit(0)
        elif choice == 3:
            print("Wrong answer. The espace pod explodes with you inside it.")
            print("Hint: 1st the worst, 2nd the best, 3rd the one with the hairy chest.")    
            exit(0)
        else:
            print("That's not a number.")
            exit(0)


class Map(object): # The map will state the scene.

    def __init__(self, start_scene): # start scene of the map. 
        self.start_scene = start_scene    

    def next_scene(self, scene_name): # next scene of the map.
        # should return an instance of the scene based on the scene name.
        if scene_name == 'central corridor':
            return CentralCorridor()
        elif scene_name == 'laser weapon armory':
            return LaserWeaponArmory()
        elif scene_name == 'the bridge':
            return TheBridge()
        elif scene_name == 'escape pod':
            return EscpaePod()
        else:
            exit(0)

    def opening_scene(self): # opening scene.
        print(self.start_scene)

# test
a_map = Map('central corridor')  
a_game = Engine(a_map)
a_game.play() 

a_map = Map('laser weapon armory') 
a_game = Engine(a_map)
a_game.play()

a_map = Map('the bridge') 
a_game = Engine(a_map)
a_game.play()

a_map = Map('escape pod') 
a_game = Engine(a_map)
a_game.play()

