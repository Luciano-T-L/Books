# Functions and Variables

# defining the functions using two arguments. the function print the argumest with some text.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Giving directly the values of the arguments.
print("We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

# Using variables...
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# ... to use in the fuctions
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Doing math with de arguments for the fuction
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# mixing variables and math for the variables in the fuction
print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10)




#S