ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: 
    next_one = more_stuff.pop() # removes and returns element from more_stuff, also --> more_stuff.pop() in python when the pop fucntion is run it adds an extra argument i.e. pop(more_stuff).
    print("Adding: ", next_one) 
    stuff.append(next_one) # adds next_one to end of the 'stuff' list. i.e. the 'ten_things' list
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # prints the last element 
print(stuff.pop()) # removes and returns the last element 
print(' '.join(stuff)) # returns list joined together --> concatenates the strings, returns a new string.
print('#'.join(stuff[3:5])) # concatenates strings with # in the middle of them, stuff[3:5] is a list slice that extracts elements at index 3 and 4 but not 5. Like range(3, 5)

"""
When to use lists:

- Need to maintain order. Not sorted order but listed order. Lists dont sort for you.
- Need to access contents randomly, using cardinal numbers starting at 0.
- Need to go through contents linearly, (first to last). Remember that's what a for-loop is for.
"""

"""
Notes From Study Drills:

What is Object Orientated Programming? https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

What are the 4 principles of object-oriented programming?
- encapsulation
- abstraction
- inheritance 
- polymorphism 
"""