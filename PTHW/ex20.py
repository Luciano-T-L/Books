# Functions and Files

# Importing
from sys import argv

# Giving the argument
script, input_file = argv

# Creating read funcition
def print_all(f):
    print(f.read())

# Creating rewid function
def rewind(f):
    f.seek(0)

# Priting line function
def print_a_line(line_count, f):
    print(line_count, f.readline(), end ='')

# Opening the file
current_file = open(input_file)

print("Fisrt let's print whole file:\n")

#Printing all file
print_all(current_file)

print("\n")
print("Now let's rewind, kind of a tape.\n")

# Rewind the cursor
rewind(current_file)

print("Let's print three lines:")

# priting line 1
current_line = 1
print_a_line(current_line, current_file)

# Priting line 2 (current line + 1 = 2)
current_line += 1
print_a_line(current_line, current_file)

#Priting line 3 (current line + 1 = 3)
current_line += 1
print_a_line(current_line, current_file)
