"""def Loop(times, increment):

    i = 0
    numbers = []

    while i < times:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


Loop(10, 2)"""

def Loop_for(times, increment):
    numbers = []

    for x in range(0, times, increment):
        numbers.append(x)

    return numbers

print(Loop_for(6, 1))