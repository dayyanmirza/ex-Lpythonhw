# # Composition:

# class Other(object):

#     def override(self):
#         print("OTHER override()")

#     def implicit(self):
#         print("OTHER implicit()")

#     def altered(self):
#         print("OTHER altered()")

# class Child(object):

#     def __init__(self):
#         self.other = Other() # creates an instance of the Other() class --> assigned to the self.other attribute

#     def implicit(self):
#         self.other.implicit() # used to access the Other class implicit function. 

#     def override(self):
#         print("CHILD override()")

#     def altered(self):
#         print("CHILD, BEFORE OTHER altered()")
#         self.other.altered() # used to access the Other class altered function
#         print("CHILD, AFTER OTHER altered()")

# son = Child()

# son.implicit()
# son.override()
# son.altered()

"""
Study Drills:

https://peps.python.org/pep-0008/

- Read the above and try applying it to your code. 

"""      
  