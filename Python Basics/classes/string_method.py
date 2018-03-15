'''We can use the __str__ method to convert a class instance into a
string, so that printing the class name directly will return a
string of our choice, instead of useless information'''

'''Here is a class without a __str__ method:'''

class testclass(object):

    def placeholder(self):
        pass

x = testclass()
print x   #returns '<__main__.testclass instance at 0x7f45187fa7a0>'


'''Here is a class with a __str__ method:'''

class testclass2:

    def __str__(self):
        return "Something Useful"

x = testclass2()
print x     #returns the string we chose, 'Something Useful'

'''We can also create use the __repr__ method to allow a user to
directly print something of our choice in an interactive session'''
