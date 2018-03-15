#We can create a custom error message when something goes wrong using a
#try command as follows:

#We'll check if a variable can be converted to a float

variable = "Hello"

try:
    variable = float(variable)
except ValueError:
    print "Variable cannot be converted to float"

#There are many different types of errors, be sure you know which one to
#use when throwing an exception

try:
    a = "a" + 3    #This piece of code would normally crash the
except:             #program, using a try/except will prevent this
    pass

#We can throw a custom error like so:

try:
    a = "a" + 3
except TypeError:                       #Only TypeErrors will be handled
    raise TypeError ("You dun goofed")
