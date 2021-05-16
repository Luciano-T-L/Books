# Creating a variable that contains four arguments
formatter = "{} {} {} {}"

# Passing differents possibles arguments for my variable
print(formatter.format(1, 2, 3, 4))  # int
print(formatter.format("one", "two", "three", "four"))  # strings
print(formatter.format(True, False, False, True))  # booleans
print(formatter.format(formatter, formatter, formatter, formatter))  # the variable itself
print(formatter.format(
    "In all chaotic beauty lies a wounded work of art.",
    "Beautiful but torn, wreaking havoc on my heart.",
    "Camouflaged by insecurities, blinded by it all.",
    " I love the way you sit there and barely notice me at all."
))
