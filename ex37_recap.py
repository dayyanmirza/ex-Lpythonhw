# Keywords: The rest of the information is in ex37 or here --> https://newcastle-my.sharepoint.com/personal/c1014579_newcastle_ac_uk/_layouts/15/Doc.aspx?sourcedoc={1e5086bf-c196-4ebb-9aec-d2a2893f685f}&action=edit&wd=target%28LearnPython3TheHardWay.one%7C1fcd8a64-3890-6b42-a421-889545748676%2FEx%2037%20Symbol%20Review%7Cceba3044-de32-fe40-b9a7-0c2af1c190eb%2F%29&wdorigin=NavigationUrl

"""
and - logical and
"""


"""
as - used to create an alias i.e.:

also can do a with as statement i.e. with X as Y: pass --> this makes X as Y i.e. can use Y instead of X, similar to below when I did import calendar as c you can type c to use the calendar functionality.

i.e.
# using with statement

with open('file_path', 'w') as file:
    file.write('hello world !')

i.e.
import calendar as c
 
print(c.month_name[1])
"""


"""
assert - will test if a condition returns true or not, if not an AssertionError is raised.

i.e. 
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"

"""



"""
break - helps you break out of a for or while loop

i.e. 
for i in range(9):
  if i > 3:
    break
  print(i)

i.e.
i = 1
while i < 9:
  print(i)
  if i == 3:
    break
  i += 1

"""


"""
class - a class is has different attributes like name and age i.e. which can be used to create objects like p1 below.

for look into classes and objects check out https://www.w3schools.com/python/python_classes.asp and this page has some info on it https://newcastle-my.sharepoint.com/personal/c1014579_newcastle_ac_uk/_layouts/15/Doc.aspx?sourcedoc={1e5086bf-c196-4ebb-9aec-d2a2893f685f}&action=edit&wd=target%28Udacity%20Course%20Data%20Structures%20and%20Algorithms.one%7C9764177d-09d2-49fa-91f4-817b8b5694a3%2FUdacity%20Course%20-%20Data%20Structures%20%20Algorithms%7Cfc8e9fb8-3b56-4876-b80b-279eb2a4cf4c%2F%29&wdorigin=NavigationUrl

i.e. 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"""


"""
continue - is used to skip the current iteration, in a for or while loop, and continues to the next iteration.

i.e.
for i in range(9):
  if i == 3:
    continue
  print(i)

i.e. 
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)

"""



"""
def - defines a function

def X(): 
    print("hello")
"""



"""
if, elif, else - conditions
"""


"""
except -  lets you handle the error (check out w3schools for more information -> https://www.w3schools.com/python/python_try_except.asp)

#The try block will generate an error, because x is not defined:

i.e. 
try:
  print(x)
except:
  print("An exception occurred")


i.e. 
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

"""



"""
exec -  run a string as python, can extecute a block of code.

i.e.
x = 'name = "John"\nprint(name)'
exec(x)
"""


"""
finally - the finally block will be executed regardless of whether an error is raised in the try block or not. Used in try, except, else blocks.  --> https://www.w3schools.com/python/ref_keyword_finally.asp

i.e. 
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")

"""

"""
for - for loop. Set a condition for which you can loop. i.e. for X in Y: pass

i.e. 
for x in range(6):
  print(x)
else:
  print("Finally finished!")
"""

"""
from - import specific parts of a module.

from x import y
"""


"""
global - declares that you want a global variable.

- global variables are ones which are created outside a function whereas local variables are inside of a function:
- Global means the variable can be accessed outside and inside a function whereas local can only be accessed inside a function.
- Normally, when you create a variable inside a function that variable is local.
- If you want to create a variable inside a function with a global scope then simply use the global keyword.

For more examples check out --> https://www.w3schools.com/python/python_variables_global.asp

i.e. 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


- If you want to change the value of a global variable inside a function, refer to the variable by using the global keyword

i.e. 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""


"""
import - imports a module i.e. import os 

i.e. from sys import argv, imports specific parts of a module. Whereas import --> imports a module to use i.e. import os.
"""

"""
in - has two purposes: --> 1) to check if a value is in a sequence (list, range, string etc.) --> 2) used to iterate through a sequance in a for loop. https://www.w3schools.com/python/ref_keyword_in.asp

i.e. demonstrates purpose --> 1)

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
  print("yes")


i.e. demonstrates purpose --> 2) 

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
"""



"""
is - The is keyword is used to test if two variables refer to the same object.  https://www.w3schools.com/python/ref_keyword_is.asp#:~:text=The%20is%20keyword%20is%20used,if%20two%20variables%20are%20equal.


- The test returns True if the two objects are the same object:
i.e. This example returns True:

x = ["apple", "banana", "cherry"]

y = x

print(x is y)



- The test returns Flase if they are not the same object, even if they are 100% equal:
i.e. This example returns False:

x = ["apple", "banana", "cherry"]

y = ["apple", "banana", "cherry"]

print(x is y)

"""



"""
lambda - is used to create a small anonymous function.

- The lambda function can take any number of arguments but can only have one expression.


i.e. Returns 15.

x = lambda a : a + 10

print(x(5))


i.e. Returns 14

x = lambda a, b, c : a + b + c

print(x(5, 6, 3))
"""


""" 
not - logical not i.e. not True == False
"""

"""
or - logical or i.e. True or False == True 
"""

"""
pass - used as a palaceholder for future code. https://www.w3schools.com/python/ref_keyword_pass.asp

- Doesn't do anything when executed, just useful when theres a piece of code that can't be empty like a function, class or an if statement etc.

i.e. 
def myfunction():
  pass


i.e.
class Person:
  pass


i.e. 
a = 33
b = 200

if b > a:
  pass
"""

"""
print - to print stuff i.e. print("hello")
"""



"""
raise - raise keyword is used to raise an exception, when things go wrong. https://www.w3schools.com/python/ref_keyword_raise.asp

- You can define what kind of error to raise and the text to print to the user.


i.e. Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


i.e. Raise a TypeError if x is not an integer
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

"""



"""
return - Exit the function with a return value. https://www.w3schools.com/python/ref_keyword_return.asp

i.e. Returns 6

def myfunction():
  return 3+3

print(myfunction())

"""



"""
try - try this block and if a exception go to except. https://www.w3schools.com/python/ref_keyword_try.asp#:~:text=The%20try%20keyword%20is%20used,went%20wrong%2C%20see%20examples%20below.

- try is used in try...except blocks. Its used to test a block of code, you can define different blocks for different error types and blocks to execute if nothing went wrong.

i.e. Try a block of code, and decide what to to if it raises an error:

try:
  x > 3
except:
  print("Something went wrong")


i.e. Raise an error and stop the program when there is an error in the try block:

try:
  x > 3
except:
  Exception("Something went wrong")
"""


"""
while - while loop https://www.w3schools.com/python/python_while_loops.asp

i.e. 
i = 1
while i < 6:
  print(i)
  i += 1
"""


"""
with - used to create an alias i.e.:

also can do a with as statement i.e. with X as Y: pass --> this makes X as Y i.e. can use Y instead of X, similar to below when I did import calendar as c you can type c to use the calendar functionality.

i.e.
# using with statement

with open('file_path', 'w') as file:
    file.write('hello world !')

"""



"""
yield - Pause here and return to caller.  `yield` keyword makes a function into a generator. 

- Python keeps the call stack for the generator function open and saves the state. When you invoke the next() function it will return execution to the same point it left off in the generator function. As shown in the Generators from Generator Expressions example below.

i.e. Generators from Generator Expressions
- Similar to List Comprehensions, but uses ( ) rather than [ ].
- Create with a single line of code.
- Only use 120 bytes of memory.

# example:
gene = (x for x in range(999999))

import sys
print(sys.getsizeof(gene))
print(type(gene))

print(next(gene))
next(gene)
next(gene)
print(next(gene)) 

This code outputs:
120
<class 'generator'>
0
3

For more information check out --> https://github.com/joeyajames/Python/blob/master/Python%20Generators.ipynb or https://www.youtube.com/watch?v=Bzfu83LiEZs&ab_channel=OggiAI-ArtificialIntelligenceToday

# The yeild keyword and generators:

Generator function doesn't stop really it stays open. 

i.e. The while loop continues indefinitely. The function increments x then goes back through the while loop and returns x w/ each iteration.

def my_generator(x=1):
    while True:
        yield x
        x += 1

Then you can use the my_generator function so any variable assigned to my_generator can run indefinitely.

The advantage generators have over lists:
- Generator can provide and infinite sequence. 
- Generator doesn't load values into memory. (Only stores one number at a time. Very small call stack.)

i.e.
import time
gene = my_generator()
print(type(gene))

for i in gene:
    print(i, end=' ')
    time.sleep(0.5) 


# Using the generator with explicit next( ) calls
i.e. each iteration of the for loop it calls the generator using next(gene) --> check out the links above for more info.

gene = my_generator()
print(gene.__next__())
for i in range(10):
    print(next(gene), end=' ')



i.e. Generator to Read File
Saves memory, and avoids memory overflow for very large files, because it only loads one line into memory at a time.

def read_file(fn = 'bands.txt'):
    for line in open(fn):
        yield line
  
band = read_file()
print(next(band))
for i in range(6):
    print(next(band), end='')
"""
    

# String format example:
"""
# String format example:

num = 20 

print("%d!" % num)
"""


