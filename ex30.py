people = 30
cars = 40
trucks = 50

# Checks if cars is greater than people, the other if, elif, else statements are self explanatory... 
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if trucks > people or trucks > cars:
    print("Soo many trucksssssssssss.")