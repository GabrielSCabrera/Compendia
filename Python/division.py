#Make sure to add this line at the beginning of a program
#where you might divide integers, otherwise they wil be
#rounded to the nearest integer in the case of decimals

from __future__ import division

a = 1
b = 2

c = a/b

print c

#This will display the correct answer, removing __future__.division will
#round the answer to 0, instead of 0.5
