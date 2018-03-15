import numpy     #Arrays are not standard in Python, and require numpy

n = 5
array_type = "int"

array = numpy.zeros(n, array_type)  #Creates a blank array of length n
                                    #and given type

array2 = numpy.zeros_like(array)    #Creates a blank array of the
                                    #same length as given array

#We can also convert lists to arrays with the following command:
array_list = [1,2,3,4,5]

array = numpy.array(array_list)

#To create an array with n uniformly distributed elements in an
#the interval [p,q] use the linspace command

p = 1
q = 5

array = numpy.linspace(p,q,n)

#To access elements of the array use the same commands as those
#used for lists

index = 0

element = array[index]

#We can vectorize arrays and run operations on them directly

array = array + n          #This is just an example, all mathematical
                           #operations in the math library are
array = numpy.sqrt(array)  #available to arrays, just call the numpy
                           #module instead of math
