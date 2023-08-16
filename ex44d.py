# All three combined 
class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()") 


class Child(Parent):

    def override(self): # override function in the Child, if called, overrides the override function of the Parent.
        print("CHILD override()") 

    def altered(self): # altered function in Child overrides the one in the parent.
        print("CHILD, BEFORE PARENT altered()") 
        super(Child, self).altered() # runs the Parent altered function  
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit() # implicit function of Parent runs 
son.implicit() # implicit function of Parent runs as Child doesn't have a implicit function

dad.override() # Parent override function runs
son.override() # Child override fucntion runs 

dad.altered() # Parent alterered function runs 
son.altered() # Child altered function runs


"""

Using super() with __init__:

The most common use of super() is actually in __init__ functions in base classes. 
This is usually the only place where you need to do some things in a child, then complete the initialization in the parent. 
Here's a quick example of doing that in the Child:

i.e.

class Child(Parent):
def __init__ (self, stuff):
    self.stuff = stuff
    super(Child, self).__init__()

This is pretty much the same as the Child.altered example above, except I'm setting some variables in the __init__ before having the Parent initialize with its Parent.__init__.”

"""