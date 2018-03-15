'''Oftentimes we can add two objects of the same type using the '+'
operator, for example ints or lists.  Since we can create new types
using classes, we can set them to perform a function with the '+'
operator as well:'''

class addition(object):

    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        return "%s and %s" %(self.string, other)

    def __str__(self):
        return self.string

obj_a = addition("First Thing")
obj_b = addition("Second Thing")

print obj_a + obj_b #returns 'First Thing and Second Thing'

'''We can do the same with multiplication and other operators,
here is a list of those available:'''

''' a+b     :       a.__add__(b)
    a-b     :       a.__sub__(b)
    a*b     :       a.__mul__(b)
    a/b     :       a.__div__(b)
    a**b    :       a.__pow__(b)

    b+a     :       a.__radd__(b)
    b-a     :       a.__rsub__(b)
    b*a     :       a.__rmul__(b)
    b/a     :       a.__rdiv__(b)

    len(a)  :       a.__len__()
    abs(a)  :       a.__abs__()

    a==b    :       a.__eq__(b)
    a!=b    :       a.__ne__(b)

    a>b     :       a.__gt__(b)
    a>=b    :       a.__ge__(b)

    a<b     :       a.__lt__(b)
    a<=b    :       a.__le__(b)

    -a      :       a.__neg__()

    is a    :       a.__bool__()

    *note, if a function __bool__ is not defined and returning either
    True or False, __len__ is called to check if len(a) is zero and
    returns False is len(a) is zero, and True otherwise.
