things = "Lighter Tobacco Skin Cellphone Glasses Book Calculator"
print(things)
list = things.split(' ')
print(list)

list.append("Photograph")
print(list)

pop1 = list.pop()
print(pop1)
print(list)

list.insert(1, "Control")
print(list)

print('#'.join(list[0:2]))
print(list)