from sys import argv 
from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

#open and read the from_file from argv input.
in_file = open(from_file).read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")

#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#open and write the from_file input to the to_file.
out_file = open(to_file,'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
