'''Attribute checking:'''

'''Our class has no constructor, which is bad practice but doable'''

class testclass(object):
    def function_in_class(self, x = None):
        if x is not None:
            self.x = x
        if not hasattr(self, 'x'):
            print "must enter value for x"
            return None
        return self.x * 5

x = testclass()
x.function_in_class()   #returns "must enter value for x"

'''We can also use a try except block:'''

class testclassb(object):
    def function_in_class(self, x = None):
        if x is not None:
            self.x = x
        try:
            value = self.x * 5
        except:
            msg = "You cannot call this function without x"
            raise TypeError(msg)
        return value

y = testclassb()
y.function_in_class()   #raises a TypeError with our msg above
