from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename, "r")

print(target.read())