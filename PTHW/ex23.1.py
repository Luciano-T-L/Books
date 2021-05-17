# Testing somethings

from io import StringIO

string = open("test.txt", encoding="utf-8")

line = string.read()

x = line.encode("utf-16", "strict")

print(x)

w = x.decode("utf-16", "strict")

print(w)