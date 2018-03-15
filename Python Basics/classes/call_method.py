'''We can use the __call__ method to use a class outright:'''

class testclass(object):

    def __call__(self, x):
        return x * 5

'''Now we can call testclass directly:'''

func = testclass()
val = func(5)   #returns 25, makes it unnecessary to name a function
val = func.__call__(5)  #Does the same as above

'''We can test if testclass is callable as follows:'''

if callable(testclass):
    print "Callable"
else:
    print "Not Callable"
print
