# More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
#sdsa
