class MyStuff(object): # sidenote: Python is considered an object-oriented programming language

    def __init__(self): # 2. init initialses newly created empty object 
        self.tangerine = "And now a thousand years between" # 3. self is the empty object, and you can set varibales on it like you would for a module, (dictioray) or other object i.e. use the . (dot) operator
        # 4. set self.tangerine to a string and now you've initialised this object.  
        # 4. (continued) Python can take this new object and assigns it to the thing variable for you to work with it.                                                  
    def apple(self):
        print("I AM CLASSY APPLES!")
    
# The class is used as a blueprint to make objects.

thing = MyStuff() # 1. Python looks for the class MyStuff(), when it sees its a class then an empty object is created, w/ the functions specified in the class.
thing.apple()
print(thing.tangerine)    