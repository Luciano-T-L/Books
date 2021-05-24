"""mystuff = {'apple', 'I am apples!'}
print(mystuff['apple'])
"""
# this goes in mystuff.py
def apple():
    print("I am apples!")

# This is a variable
tangerine = 'Living reflection of a dream'

class MyStuff(object):

    def __init__(self):
        self.tangerine = 'And now a thousand years between'
    
    def apples(self):
        print('I am classy apples!')

thing = MyStuff()
thing.apples()
print(thing.tangerine)

"""
# get things from things:

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)
"""

# class style

thing = MyStuff()
thing.apples()
print(thing.tangerine)