# Reading and Writing Files

# Importing argv
from sys import argv

# Using filename as a argument to enter
script, filename = argv

# Printing
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C) .")
print('if you do want that, hit RETURN.')

# Getting the answer
input("?")

# Opening file as write mode
print("Opening the file...")
target = open(filename, 'w')

# Truncating file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# Getting inputs for the file
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Now i'm gointo to write these to the file.")

# Writing the inputs in the file
target.write(f"{line1}\n{line2}\n{line3}")

# Closing file
print("And finally, we close it.")
target.close()
