## Animal is-a object
class Animal(object):
    
    def printing(self):
        print("This is a animal!")

## Dog is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a name
        self.name = name
    
    def printing(self):
        print("This is a Dog")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
    
    def printing():
        print("This is a cat")


## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## Employee is-a Person that has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Kalibut is-a Fish:
class Halibut(Fish):
    pass


## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet "Satan"
mary.pet = [satan, rover]

# Frank os a Employee that has-a salary
frank = Employee("Frank", 120000)

## Frank has-a pet "Rover"
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut

rover.printing()

mary.pet()