# Reading Files

# Use argv to get a file name
from sys import argv

script, filename = argv

# Opening the file
txt = open(filename)

print(f"Here's your file {filename}:")
# File comand  .namecommand(parameters)
print(txt.read())

# Opening other .txt with input
print("Type the filename again:")
file_again = input("> ")

# Opening file
txt_again = open(file_again)
# Printing the content
print(txt_again.read())
