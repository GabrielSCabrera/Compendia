'''We can dump all the contents used in a class with the __dict__
dictionary:'''

class one(object):
    '''Our docstring'''
    def __init__(self, value, otherthing):
        self.value = value
        self.other = otherthing

    def dump(self):
        print self.__dict__

a = one("a",5)
a.dump()    #returns {'other': 5, 'value': 'a'}

'''We can use dir(a) to get more info on our instance's contents'''

print dir(a) #returns the following:
#['__doc__', '__init__', '__module__', 'dump', 'other', 'value']


'''We can use the __doc__ variable to get our docstring:'''

print a.__doc__ #returns 'Our docstring'

'''We can get the name of the module our class is defined in, by
using the __module__ variable.  If the class is in our program,
it will simply return "__main__"'''

print a.__module__  #returns '__main__'
