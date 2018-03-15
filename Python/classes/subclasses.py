'''We can create a class with access to all the functionality of
another class, in the form of a "subclass"'''

class superclass(object):

    def __init__(self,a,b,c):
        self.a,self.b,self.c = a,b,c

    def __call__(self,x):
        return x**2

    def one(self,x):
        return x+self.a+self.b

    def two(self,y):
        return y-self.c

class subclass(superclass):

    def __init__(self,a,b,c,d):
        superclass.__init__(self,a,b,c) #superclass initializes a,b,c
        self.d = d
    #We can call a method or object from superclass in two ways:
    def __call__(self,x,y):
        p = superclass.one(self, x)#Calls 'one' from superclass

        q = super(subclass, self).two(y)#Calls 'two' from superclass
        return p+q
