'''Classes are very useful for creating new types, and for creating
comprehensive formulas etc...'''

'''We must remember to use 'constructors' such as __init__ or
__self__ when setting up a class, and to properly indent'''

'''The following class contains several functions that can be
called in conjunction with the class, and extract different pieces
of information, such as what the class does, or contains, etc...'''

class ClassName(object):

    '''Here goes the doc string explanation'''

    def __init__(self, argument_a):
        self.var_a = argument_a    #All global variables must go here,
        self.var_b = 10            #__init__ and self are important!

    def func_a(self, argument_a):  #Once again, remember 'self'
        return self.var_a * argument_a * self.var_b

    def func_b(self):
        return "%d * argument_a * %d" %(self.var_a, self.var_b)

'''We can now create a new variable of type 'ClassName' with an
'argument_a' value of, for example, 30'''

var = ClassName(30)

'''We can use this new ClassName type variable with argument_a = 10 to
get some other useful information out of the class'''

func_a_result = var.func_a(20)  #returns '6000'
explanation = var.func_b()      #returns '30 * argument_a * 10'
