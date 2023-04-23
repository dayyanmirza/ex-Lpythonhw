# Strings, Bytes, and Character Encodings
import sys 
script, encoding, error = sys.argv
# (Page 130 ex23 breaks down line-by-line what the code does.)
# Go through and comment above everything saying what it does:

# main function, reads one line from the languages file it's given.
def main(language_file, encoding, errors):
    line = language_file.readline()

# Main is returned in the main function as a function is simply a jump to the top of where you’ve named it main, then calling the function at the end of itself would jump back to the top and run it again.
# Making a loop and the if statement prevents it from running forever, i.e. when an empty string is returned it doesn’t run line 9 and 10. 

# if statement (tests the truth of a variable and based on the truth it either i.e. runs the picee of code or not.) 
# Checks if line has something in it.
# When it returns the main function it then jumps back to the top of the function main and loops round to the next line. The if statement in main stops it looping forever, i.e. stops when an empty string is returned.
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    

# print_line function does the actual encoding of each line from the languages.txt file.
def print_line(line, encoding, errors):
    next_lang = line.strip() # this is a simple stripping of the trailing \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors=errors) # next_lang variable is a string, must encode strings to get raw bytes. (finally encode the language you've recieved from the languages.txt file.), you pass to encode() the encoding you want and how to handle errors.
    cooked_string = raw_bytes.decode(encoding, errors=errors) # raw_bytes it bytes, DBES, decode bytes, must decode raw bytes to get a Python string, the string should be the same as the next_lang variable.

    # the raw bytes are the python numerical bytes that are used to store the string, these raw bytes are then displayed 'cooked' in your terminal i.e. the real characters are displayed in terminal.
    # print them both out to show what they look like.
    print(raw_bytes, "<===>", cooked_string)

# Done defining functions so now I want to open the languages.txt file.
languages = open("languages.txt", encoding="utf-8")

# The main function is then run (w/ all correct paramaters and kick starts the loop) and rememeber it will jump to the beggining of the main function and then keep looping because it returns main at the bottom of the main function, the if statement (if line:) prevents the function from looping forever.
main(languages, encoding, error)