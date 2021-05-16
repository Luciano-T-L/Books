# Variable 1
cars = 100
# Variable 2
space_in_a_car = 4.0
# Variable 3
drivers = 30
# Variable 4
passagenrs = 90
# Variable 5
cars_not_driven = cars - drivers # Empty cars
# Variable 6
cars_driven = drivers 
# Variable 7
carpool_capacity = cars_driven * space_in_a_car  # transport capacity
# Variable 8
average_passagenrs_per_car = passagenrs / cars_driven  # average of passagenrs per car


# Printing how many cars are available
print("There are", cars, 'cars available.')
# Printing the number of available drivers
print("There are only", drivers, "drivers availabe.")
# Printing the number of empty cars
print("There will be", cars_not_driven, "empty cars today.")
# Printing how much people can be transproted
print("We can tranport", carpool_capacity, "people today.")
# Priting who many carpool is avaible
print("we have", passagenrs, "to carpool today.")
# Priting how may passenger can be put in each car
print("We need to put about", average_passagenrs_per_car, "in each car.")
