# Exercise 13. Parameters, Unpacking, Variables.

from sys import argv
script, first, second, third = argv  # argument variable

print("The script is called:", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# How you shold run in cmd
#->python ex.13.py first 2nd 3rd

print("Those are the best three things that you can think of?")

x = input("Try again your first variable: ")
y = input("And your second: ")
z = input("The last one: ")

print(f"{x}, {y}, {z}. Much better!")