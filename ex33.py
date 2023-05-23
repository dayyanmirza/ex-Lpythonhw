def while_loop(x, y):
    i = 0 
    numbers = []

    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i) # append adds i to the numbers list above.

        i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(6, 1)