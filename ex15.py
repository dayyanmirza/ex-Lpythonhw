#from sys import argv

# takes arguments when running script.
#script, filename = argv 

print("Input filename: ")
filename = input(">")

# opens the file that was inputted in argv. makes a file object 
txt = open(filename)

# Prints out the file that was inputted in argv.
print(f"Here's your file {filename}:")
# reads the file without parameters.
print(txt.readline())
txt.close()

# Asks you to type filename again. And file_again variable asks for input.
print("Type the filename again:")
file_again = input(">")

# Then the txt again opens the file inputted in file_again. 
txt_again = open(file_again)

# Then file_again inputted file is read (where read has no parameters).
print(txt_again.read())
txt_again.close()