def while_loop(y):
    i = 0 
    numbers = []

    # using for-loop instead of while loop
    for i in range(0, 6):
        print(f"At the top i is {i}")
        numbers.append(i) # append adds i to the numbers list above.

        i = i + y # when you use a for-loop the increment here doesn't impact the numbers list, just changes i at the bottom. 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(1)