people = 30
cars = 30
trucks = 45

# Are there more cars than people?
if cars > people:
    print("We should take the cars.")
# Are there more people than cars?
elif cars < people:
    print("We should not take the cars.")
# are the number of cars and people the same?
else:
    print("We can't decide.") 

# Are there more trucks than cars?
if trucks > cars:
    print("That's too many trucks")
# Are there more cars than trucks? 
elif trucks < cars:
    print("Maybe we could take the trucks")
# Are the number of cars and trucks the same?    
else:
    print("We still can't decide")

# Is the number of people greater than that of trucks?
if people > trucks:
    print("Alright, let's just take the trucks.")
# Is the number of trucks greater or equal to that of people?
else:
    print("Fine, let's stay home then.") 

# Trying more complex boolean expressions

if cars == trucks or people == cars:
    print("That's True")
else:
    print("That's False, will not print")

if cars == people and trucks < cars:
    print("That's False, will not print")
elif cars == people and trucks < cars:
    print("That's True, will print")
else:
    print("There's a lot of others possibilitys, so will print.")