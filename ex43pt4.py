# Zed Shaw's Solution:
# “Gothons from Planet Percal #25”
from sys import exit 
from random import randint 
from textwrap import dedent 

class Scene(object): # base class --> Scene 

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map): # The constructor initialises the Engine instance. It takes a single argument scene_map.
        self.scene_map = scene_map

    def play(self):  
        current_scene = self.scene_map.opening_scene() 
        last_scene = self.scene_map.next_scene('finished')
        
        """
        The play method is responsible for the gameplay loop:
        - current_scene --> Starts by getting the initial scene using opening_scene() method of the Map instance a_map. Returns instance of the initial scene. 
        - last_ scene --> Gets the scene that signifies the end of the game. Using next_scene('finished') method of the Map instance.
        - Inside the while loop: 
            - The enter() method of the current_scene is called. This method returns the name of the next scene it should transition to based on their choices in that scene. This next_scene_name is stored in the next_scene_name variable. 
            - current_scene = self.scene_map.next_scene(next_scene_name) --> The next_scene method of the Map instance is called with the next_scene_name, obtained from the previous step.
                - This method returns the scene object associated with the provided scene name. 
                - The current_scene is then updated to this new scene object and the loop continues.


        """

        while current_scene != last_scene: # While loop runs as long as the current_scene is not equal to the last_scene. 
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene 
        current_scene.enter() # after the loop the final scene is played one more time to ensure the player sees the outcome of their choices before the game concludes.


class Death(Scene):

    quips = [
        "You died. Oh well try again, it's just a game.",
        "I have a small kitten thats better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. 
            You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod. 
                     
            You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you.
                """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you.
                """))
            return 'death'
        
        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, then bursts out laughing and can't move. While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door.
                """))
            return 'laser_weapon_armory'
        
        else: 
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
        

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits.
            """))

        # cheat code: just make code = '123'
        code = f"{randint(1,9)}{randint(1, 9)}{randint(1, 9)}" 
        guess = input("[keypad]> ") # inital guess not part of the loop
        guesses = 1 # initialise guesses to 1 so that the loop only allows 9 guesses as the loop doesn't count the user input as a guess.
        
        # 1-9 --> 9 guesses allowed in the loop, plus the inital guess on the line--> guess = input("[keypad]> "), therefore there's 10 guesses in total.                            
        while guess != code and guesses < 10: 
            print("BZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.
                """)) 
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You decide to sit there, and finally the Gothons blow up the ship from their ship and you die.
                """))
            return 'death'
        


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off.
            """))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.                  
                """))
            return 'death'
        
        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin can.
                """))
            
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'
        

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take. Some of them could be damaged but you don't have time to look. There's 5 pods, which one do you take?
            """))
        
        good_pod = randint(1,5)
        guess = input("[pod #]> ")
        # cheat code: just make good_pod = 2

        if int(guess) != good_pod:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button. The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.
                """))
            return 'death'
        else:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button. The pod easily slides out into space heading to the planet below. As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. You won!
                """))
            
            return 'finished'
        

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'
    

class Map(object):

    # The scenes dictionary allows you to easily map scene names to their corresponding objects. Instead of having to manually instantiate each scene when needed i.e. x = CentralCorridor() etc, you can retrieve the appropriate scene object from the dictionary using the scene name as the key.
    scenes = { 
        'central_corridor': CentralCorridor(),  
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),  
    }

    """ 
    How does returning the next room work ?

    - It's done by using the next_scene method ot the Map class.
    - The scenes dictionary containes the scene name mapped to the scene object, each scene object is an instance a scene class i.e. CentralCorridor etc.
    - The next_scene method takes one argument which is the scene_name of the next scene you want to transition to.
    - Map.scenes.get(scene_name) --> this line in the next_scene method uses the get method retrives a scene object depedning on the scene name. If the scene name has a corresponding scene object in the dictionary the method returns the corresponding scene object, otherwise, it returns none.
    - Then it returns the retrieved scene object as a result of the next_scene method. i.e. return val. 
    """

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene) # refers to the first scene that's inputted i.e. central_corridor, i.e. in the init constructor, returns the instance of i.e. central_corridor scene. 
    

# creating an instance of the Map and Engine class and invoking the play method of the engine class.
a_map = Map('central_corridor')
a_game = Engine(a_map) # passing the instance of the map class as an agrument in the Engine class instance means the Engine class has access to the Map Class. Allowing us to navigate through the different scenes.
a_game.play()


"""
Study Drill Notes:

Finite State Machines:

# Resources:
- https://en.wikipedia.org/wiki/Finite-state_machine
- https://www.youtube.com/watch?v=9YnjgXmv6fU
- https://medium.com/@mlbors/what-is-a-finite-state-machine-6d8dec727e2c
    - A finite state machine:
        - Is a model of computation, based on a hypothetical machine made of one or more states, fixed set of states.
        - Can only be in one state at any point in time, meaning the machine must transition from one state to another to perform different actions.

"""