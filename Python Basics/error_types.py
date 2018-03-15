#Python tends to use the following to throw errors:

import sys

sys.stderr.write("This is an error message\n"); sys.exit(1)

#sys.exit(1) tells the program to exit due to an error

'''
IndexError          : List index out of range
ValueError          : Converting an incompatible type to another
NameError           : Attempting to use an uninitialized variable
ZeroDivisionError   : Division by zero
SyntaxError         : Code is writted incorrectly
TypeError           : Object types involved in operation are incompatible
'''
