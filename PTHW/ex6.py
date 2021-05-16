# variable and value
types_of_people = 10
#string within another string
x = f"There are {types_of_people} types of people."


# variable and value
binary = "binary"
# variable and value
do_not = "don't"
# variable with two strings within another string
y = f"Those who know {binary} and those who {do_not}"

# printing variable x
print(x)
# printing variable y
print(y)

# printing a string within another string
print(f"I said: {x}")
# printing a string within another string
print(f"I also said: '{y}'")

# variable and a boolean value
hilarious = False
# variable with a boolean value within the string
joke_evaluation = "Isn't that joke funny?! {}"

# printing variable
print(joke_evaluation.format(hilarious))

# creating a variable with a string
w = "This is the left side of..."
# creating a variable with a string
e = "a string with right side."

# printing bouth strings in variables.
print(w + e)
