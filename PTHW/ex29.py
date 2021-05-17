people = 20
cats = 10
dogs = 10

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on")

if people > dogs:
    print("The world is dry!")


dogs += 1

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")


if dogs != cats:
    print("Dogs and Cats are not equal.")

if True or False:
    print("True")  # Will print

if True and False:
    print("False")  # Will not print

if not(False and False):
    print("True")  # Will print
