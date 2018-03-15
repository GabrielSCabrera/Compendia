#There are several ways to import things from other libraries

from math import pi             #Pi is imported directly as a global variable
from math import sqrt           #Sqrt is imported
from cmath import sqrt as csqrt #Imports the sqrt function from cmath but
                                #renames it to prevent clashing functions
import math                     #This gives us access to all math.x functions
import math*                    #Imports every function from math

print pi
print math.e
print sqrt(4)
print csqrt(-1)
