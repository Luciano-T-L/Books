# Doing some fuction to run it in 3 different ways!

def doing_basic_math(x, y):
    sum = x + y
    sub = x - y
    mult = x * y
    div = x / y
    
    print(f"The sum of the numbers is: {sum}")
    print(f"The subtraction of the numbers is {sub}")
    print(f"The multiplication of the numbers is {mult}")
    print(f"The division of the numbers is: {div}")

def number():
    return(2)


# Calling function
doing_basic_math(10, 2)

print("\n")

# With variables
x = 5
y = 3
doing_basic_math(x, y)

print("\n")

# Using inputs
num1 = int(input("First number: "))
num2 = int(input("Secod number: "))
doing_basic_math(num1, num2)

print("\n")

# Variables with math
var1 = 100
var2 = 200

doing_basic_math(var1 + 50, var2 / 2)

print("\n")

# math
doing_basic_math(5 + 2, 10 / 2)

print("\n")

# Function inside other function
doing_basic_math(number(), 50)

print("\n")

# Using inputs and math
num1 = int(input("First number: "))
num2 = int(input("Secod number: "))
doing_basic_math(num1 + 2, num2 ** 3)

print("\n")

# Puting the function in a variable and printing the variable
x = doing_basic_math(1, 2)
x