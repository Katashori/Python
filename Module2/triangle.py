import sys
from math import sqrt
from sys import argv
try:
	a = int(argv[1])
	b = int(argv[2])
	c = int(argv[3])
except ValueError:
	print("Please input size of every triangle's side (integer)")
p = (a + b + c)/2
try:
	s = sqrt(p*(p-a)*(p-b)*(p-c))
	print(s)
except ValueError:
    print("Incorrect data")
