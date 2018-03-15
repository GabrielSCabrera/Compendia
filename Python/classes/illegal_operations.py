'''Python conventions state that we should use a single underscore
to name functions that are not to be used outside of a class.  It is
also a convention to name a function designed to identify illegal
operations as "_illegal"'''

'''We will demonstrate an example where addition is not a legal
operation in our class'''

class illegaltest(object):

    def __init__(self, val):
        self.val = val

    def _illegal(self, op):
        print "Illegal operation '%s' for this type"%(op)

    def __add__(self, other):
        self._illegal('+')

a = illegaltest("A")
b = illegaltest("B")

c = a + b   #returns "Illegal operation '+' for this type"
