print("You wake up and realize that you are surround from zombies.")
print("and they are comming closer!")
print("""You look around and see:
#1 - A pistol
#2 - A backpack full of tools
#3 - A shovel
You only have time to pick one item!""")
action1 = input("What's you choise? \n> ")

if action1 == "1":
    print("You take the gun and realizes it's out of bullets.")
    print("You have to RUN!!!")

elif action1 == "2":
    print("You pick the beg and see a zombie really close to you")
    print("What do you do?")
    print("#1- Take a knife from the left pocket of the backpack")
    print("#2- Try find something inside the bachpack?")
    print("#3- Just run away")
    close_zombie = input("> ")

    if close_zombie == "1":
        print("You take the knife really fast and stick it in the zombie's head!")
    elif close_zombie == "2":
        print("Too slow, the zombie grabs you.")
    else:
        print("You are faster than the zombie and run away")
    
else:
    print("You take the shovel and see a zombie right in front of you")
    fight_or_beg = input("Do you want:\n1- Take a fight?\nor\n2- Try get the backpack too?\n> ")
    
    if fight_or_beg == "1":
        print("...")
    else:
        print("...")