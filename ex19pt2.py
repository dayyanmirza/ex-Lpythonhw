def chicken_masala(chicken, masala):
    print(f"We will use {chicken} chicken.")
    print(f"We will use {masala} masala.")
    print("Wow. \n")

# or we can input numbers directly into the function
print("We can give the function numbers directly:")
chicken_masala(20, 20)

# Or we can use varibles in our script
print("We can use variables in our script:")
amount_chicken = 30
amount_masala = 40

chicken_masala(amount_chicken, amount_masala)

# or we can do some maths
print("Or we can do some maths:")
chicken_masala(3 * 2, 4 + 5)

# or we can do maths and use variables
print("Or we can do some maths using the variables in our script:")
chicken_masala(amount_chicken + 10, amount_masala + 12)

# Ask for user input
print("Input the varibales --> ")
print("This is the amount of chicken:")
chicken_amount = input(int)
print("This is the amount of masala:")
masala_amount = input(int)  

chicken_masala(chicken_amount, masala_amount)

