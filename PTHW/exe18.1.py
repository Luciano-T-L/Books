# Doing a checklist function

x = input("How many time you need to study until take a break? ")
y = input("What are you studying? ")
z = input("Are you using books, videos or doing exercices? ")

def checklist(x, y, z):
    print(f"You have to study at least {x}")
    print(f"You are studying {y}, that's great!")
    print(f"And you are using {z} to study, nice choice!")

checklist(x, y, z)
