import sys
from sys import argv
try:
	x = int(argv[1])
except ValueError:
	print("Please input one integer")
if -15 < x <= 12 or 14 < x < 17 or x >= 19:
    print('True')
else:
    print('False')
