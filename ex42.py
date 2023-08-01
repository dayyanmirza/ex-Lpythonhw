## Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal(object):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name 
        #self.name = name 
        super().__init__(name)


## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        #self.name = name
        super().__init__(name)                
   
## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name 
        self.name = name    

        ## Person has-a pet of some kind 
        self.pet = None  # so self.pet attribute is set to none as a default.   

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name. (Person has-a name which is-a name of a Employee.)
        super(Employee, self).__init__(name) # same as --> super().__init__(name);  super() is used so the Employee (subclass/parent class) can inherit the init (specifically the name attribute) of the Person (superclass) class. https://www.youtube.com/watch?v=MBbVq_FIYDA
        ## Employee has-a salary 
        self.salary = salary # don't use super on this as the superclass doesn't have salary as an attribute.

# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used --> in order to access the methods of the parent class (superclass).

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
print(rover.name)

## jerry is-a Cat 
jerry = Cat("Jerry")
print(jerry.name)

## mary is-a Person
mary = Person("Mary")
print(mary.name)

## mary has-a pet named jerry
mary.pet = jerry
print(mary.pet.name)

## frank is a Employee 
frank = Employee("Frank", 120000)
print(frank.name)

## frank has-a pet named rover
frank.pet = rover 
print(frank.pet.name)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut 
harry = Halibut()

# a list has-many items 
list = ['food','apple','pear']

# a dict has-many items aswell
adict = {
    'a' : '1',
    'b' : '2',
    'c' : '3'
}


# Research from the study drills:
#
# https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object
# https://www.reddit.com/r/learnpython/comments/7vou1s/what_does_object_in_class_classnameobject_do/
# https://stackoverflow.com/questions/46636267/python-class-as-object#:~:text=Yes%20the%20class%20object%20is,functions%2C%20modules%2C%20...&text=Similarly%3A%20stackoverflow.com%2Fquestions%2F7483947%2F%E2%80%A6. --> In Python, the definition is looser; some objects have neither attributes nor methods (more on this in Chapter 3), and not all objects are subclassable (more on this in Chapter 5). But everything is an object in the sense that it can be assigned to a variable or passed as an argument to a function.
# This is so important that I'm going to repeat it in case you missed it the first few times: everything in Python is an object. Strings are objects. Lists are objects. Functions are objects. Even modules are objects. From the link above.
#
# https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
# https://en.wikipedia.org/wiki/Multiple_inheritance 
# multiple inheritance is when an object or class can inherit features from more than one parent object or parent class. --> considered ambigious as difficult to determine where the features are inherited from. --> bad practice.