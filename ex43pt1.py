# Analysis of a Simple Game Enigne (Top Down --> i.e. from idea to code)
# “Gothons from Planet Percal #25”

"""
1) Write or draw about the problem

I'm going to write a little paragraph for the game:

"Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. 
The game will be more like a Zork or Adventure type game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. 
Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map."

At this point I have a good idea for the game and how it would run, so now I want to describe each scene:
    Death - This is when the player dies and should be something funny.
    Central Corridor - This is the starting point and has a Gothon already standing there that the players have to defeat with a joke before continuing.
    Laser Weapon Armory - This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.
    The Bridge - This is another battle scene with a Gothon where the hero places the bomb.
    Escape Pod - This is where the hero escapes but only after guessing the right escape pod.



Excerpt From
Learn Python 3 the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code (Zed Shaw's Hard Way Series)
Zed A. Shaw


2) Extract Key Concepts and Research Them

I now have enough information to extract some of the nouns and analyze their class hierarchy. First I make a list of all the nouns:

• Alien
• Player
• Ship
• Maze
• Room
• Scene
• Gothon
• Escape Pod
• Planet
• Map
• Engine
• Death
• Central Corridor
• Laser Weapon Armory
• The Bridge

Excerpt From
Learn Python 3 the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code (Zed Shaw's Hard Way Series)
Zed A. Shaw

- Research the list above, check if verbs are good function names etc.

- After the research maybe restart at step one, based on new information and rewrite descripiton and extract new concepts.


3) Create a Class Hierarchy and Object Map for the Concepts

Once I have that I turn it into a class hierarchy by asking, “What is similar to other things?” I also ask, “What is basically just another word for another thing?”

“Right away I see that “Room” and “Scene” are basically the same thing depending on how I want to do things. I'm going to pick “Scene” for this game.”

Excerpt From
Learn Python 3 the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code (Zed Shaw's Hard Way Series)
Zed A. Shaw


* Map
    - next_scene # verbs
    - opening_scene # verbs 
* Engine 
    - play # verbs
* Scene 
    - enter # verbs --> put enter under scene since all scenes underneath it will inherit it and have to override it later.
    * Death
    * Central Corridor # first scene
    * Laser Weapon Army # second scene 
    * The Bridge # third scene 
    * Escape Pod # fourth scene  
     
"""  

# 4) Code the classes and a test to run them.

class Scene(object): 
    
    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):

    def enter(self, scene_enter):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass    


class EscpaePod(Scene):

    def enter(self):
        pass 


class Map(object):

    def __init__(self, start_scene):
        pass     

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# test
a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play() 

# 5) Repeat and Refine 

