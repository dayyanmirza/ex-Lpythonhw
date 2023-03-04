from sys import argv

script, filename = argv

print(f"We're going to read {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening file...")
target = open(filename)

print(f"Here's your file, {filename}:")
print(target.read())

target.close()





