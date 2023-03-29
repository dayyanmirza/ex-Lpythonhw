from sys import argv

# argv, command line inputs -> script name and input file:
script, input_file = argv

# Defined functions, one to read, one to see, argument f is read.
def print_all(f):
    print(f.read())

# seek sets the current file position in a file stream to the beginning
def rewind(f):
    f.seek(0)

# print a line, the end="" makes avoids added a space between lines when printing in the terminal.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

# the file opens an input file
current_file = open(input_file)

# The print statements explain what happens below:
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewind function sets the pointer to the beginning of the file so that the file can be read correctly.
rewind(current_file)

print("Let's print three lines:")

# prints first line
current_line = 1
print_a_line(current_line, current_file)

# prints second line
current_line += 1 
print_a_line(current_line, current_file)

# prints third line
current_line += + 1 
print_a_line(current_line, current_file)