from sys import exit

tols = []

# Creating rooms

def room1():
    choices = "# 1 - Go through right door\n# 2 - Go through left door\n# 3 - Examine room"

    print("You are in a cave now and there are two doors in front of you")
    print("What do you do?")
    print(choices)

    while True:
        choice = input("> ")

        if choice == "1":
            room3()
        elif choice == "2":
            room2(tols)
        elif choice == "3":
            print("You don't find anything worthwhile \nWhat's yout moviment?")
        else:
            print("Invalid command!")


def room2(tols):
    knife = False
    choices = ("# 1 - Go through right door \n# 2 - Go through left door\n# 3 - Examine room\n# 4 - Examine trash")

    print("You're in a dark room, you just can se another two doors in front of you and some trash in the corner.")
    print(choices)

    while True:
        choice = input("> ")
        print("")

        if choice == "1":
            room5()
        elif choice == "2":
            room4()
        elif choice == "3":
            print("You just see two doors and some trash.")
            print("")
            print(choices)
        elif choice == "4" and not knife:
            print("You find a knife! Well done.")
            print("")
            print(choices)
        elif choice == "4" and knife:
            print("You don't find anything else.")
            tols.append("Knife")
        else:
            print("Invalid command!")


def room3():
    choices = "# 1 - Go through right door\n# 2 - Go through left door\n# 3 - Examine trash"

    print("You're in a durty room, there are two doors and trash scattered throughout the room")
    print(choices)
    print("")
    guns = False

    while True: 
        choice = input("> ")

        if choice == "1":
            print("This door is locked, try the other one!")
        elif choice == "2":
            room5(tols)
        elif choice == "3" and not guns:
            print("")
            print("Nice, you find a guns!")
            print("")
            print(choices)
            tols.append("Gun")
            guns = True
            print("")
        elif choice == "3" and guns:
            print("")
            print("You don't find anything")
            print("")
            print(choices)
            print("")
        else:
            print("Invalid command!")


def room4():
    print("You see a old men in front of a door. He looks at you and says:")
    print("You can pass for this door if you awnser correctly a riddle")
    print("And you have just three gesses, if don't discover the riddle, you die!")
    print("")
    print("'What has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows?'")
    
    attempts = 3

    while attempts != 0:
        chance = input("> ")

        if chance == "montain" or chance == "Montain":
            print("Correct, you can pass now")
            room7()
        else:
            print("Wrong!")
            attempts -= 1
    
    print("You die!")
    exit()


def room5(gun):
    print("")
    print("Danger! One giant rat is running to your directions.")
    print("What will you do?")
    print("")
    
    while True:
        print(f"# 1 - Try open the door in front of you \n# 2 - Use your gun and shot it\n# 3 - Be eaten")
        print("")
        choice = input("> ")

        if choice == "1":
            print("The rat is in your way. Fight or die!")
        elif choice == "2":
            print("You shot at the rat's face and it dies!")
            print("The door opens and you see the light of the sun!")
            room8()
        else:
            print("You are dead!")
            exit()


def room6():
    print("")
    choice = input("> ")
    if choice == 1:
        print("")
    elif choice ==2:
        print("")
    else:
        print("Invalid command!")


def room7():
    print("")
    print("You find the way out, You win!")
    exit()


def room8():
    print("")
    print("You find the way out, You win!")
    exit()


room1()
