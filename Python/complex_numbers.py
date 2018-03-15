#In python, be sure to use 'j' instead of 'i' for the imaginary axis
#We need import cmath for many complex operators/functions
import cmath
import math

a = 1 + 1j          #Be sure to have a coefficient in front of 'j'!
b = complex(2,2)    #Defines a complex number '2 + 2i'

#Addition, subtraction, multiplication and division works without cmath

real_coefficient = a.real
complex_coefficient = a.imag

polar_angle = cmath.phase(a)
polar_radius = abs(a)

rectangular_to_polar = cmath.polar(a)
polar_to_rectangular = cmath.rect(1, math.pi)

e_to_the_a = cmath.exp(a)        #Takes 'e' to the power of 'a'
square_root = cmath.sqrt(a)

logarithm = cmath.log(a,b)       #Logarithm of 'a' with base 'n'
natural_logarithm = cmath.log(a) #Leaving out the 'n' makes this a natural logarithm
log10 = cmath.log10(a)           #Logarithm base 10

sine = cmath.sin(a)
cosine = cmath.cos(a)
tangent = cmath.tan(a)

arcsine = cmath.asin(a)
arccosine = cmath.acos(a)
arctangent = cmath.atan(a)

check_for_infinite_value = cmath.isinf(a)
