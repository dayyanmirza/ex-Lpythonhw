# https://developers.google.com/edu/python/lists#for-and-in

# practice

# while loop accesses the thrid element
a = ['apple','banana','carrot']
i = 2
while i < len(a):
    print(a[i])
    i += 1

# Common list methods:    

a.append('onion') # adds element to the end. Common error: does not return the new list, just modifies the original.
print(a)    

a.insert(1,'orange') # inserts element in specified index.
print(a)

b = ['cat','lion','zebra', 'orange']
a.extend(b) # adds the elements in b to the end of list a. Using + or += on a list is similar to using extend().
print(a)

print(a.index('carrot')) # Searches for an element from the start of a list and returns the index. ValueError if element doesn't appear.

a.remove('orange') # Removes the first instance of the element.
print(a)

a.sort() # sorts the list (does not return it i.e. if you do print(a.sort()) it doesn't return anything). (The sorted() function is preferred)
print(a)

a.reverse() # reverses the lists order (does not return it i.e. if you do print(a.reverse()) it doesn't return anything).
print(a)

print(a.pop(2)) # removes and returns the element at the given index. Returns the rightmost element if index is omitted (rougly the opposite of append)
print(a)

# List slices
print("\vList Slices:")
list = ['a', 'b', 'c', 'd']
print(list[1 : -1]) # prints the list w/ out the first and last element
list[2: 0] = 'z'
print(list)
# these are methods on a list object, while len() is a function that takes the list (or string etc) as an argument. 
