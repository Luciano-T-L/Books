print("""You enter a dark room with two doors.
Do you go througs door #1 or door #2 or door #3""")

door = input("> ")

if door == "1":
    print("""There's a giant bear here eating a cheese cake.
What do you do?
1. Take the cake.
2. Scream at the bear.""")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probaly better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endlees abyss at Cthulhu's retina")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Undertanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

"""else:
    print("You stumble around and fall on a knife and die. Good job!")"""

if door == "3":
    print("You see the sun rising, and trees around you")
    print("When you look around, you see a old women")
    print("# 1. Go talk to her")
    print("# 2. Keep walking into the florest")
    option1 = input("What do you do? \n> ")

    if option1 == "1":
        print("what a young person like you doing here?")
        print("Maybe you came for dinner! do you?")
        jantar = input("Yes or No?\n> ")
    
        if jantar == "Yes":
            print("You: Dinner? Yes! I'm starving")
            print("You: What's for dinner?")
            print("/n HAHAHAHAHA!, YOU")
        else:
            print("That's a shame, well, you'll have to stay for dinner!")
            print("Because you are the dinner today!! HAHAHA")
        
    if option1 == "2":
        print("When you pass for the old women, she looks to you.")
        print("And start running to your directions like a animal!")
        print("What is your play?")
        print("# 1. Take your knife")
        print("# 2. Take your gun")
        print("# 3. Run away")
        guns_run = input("> ")

        if guns_run == "1":
            print("...")
        elif guns_run == "2":
            print("...")
        else:
            print("...")