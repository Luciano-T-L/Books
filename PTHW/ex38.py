ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop(more_stuff)
# more_stuff.pop() -> Call pop for more_stuff
# pop(more_stuff) -> Call pop with argument more_stuff

    print("Adding: ", next_one)
    stuff.append(next_one)  # append(stuff, next_one)
# stuff.append(next_one) - > Call append for stuff with argument next_one
# append(stuff, next_one)-> Call apeend with stuff and next_one arguments
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Lets do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))  # join(' ', stuff)
# ' '.join(stuff) -> Call join for ' ' with argument stuff
#join(' ', stuff) -> Call join with ' ' and stuff as arguments
print('#'.join(stuff[3:5]))  # join('#', stuff[3:5])
# '#'.join(stuff[3:5]) -> Call join for '#' with stuff as argument and [3:5] as parameters of this argument
# join('#', stuff[3:5]) -> Call join with '#' and stuff as arguments and [3:5] as parameters of 'stuff' argument