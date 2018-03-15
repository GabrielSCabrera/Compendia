'''We can create variables or methods that are shared every time
a new object of the same class type is created, such as a counter
that keeps track of how many object have been created:'''

class countthing(object):
    counter = 0
    def __init__(self):
        countthing.counter += 1

a = countthing()
b = countthing()
c = countthing()

print a.counter #All of these print out the same number: 3
print b.counter
print c.counter

'''We can also have entire methods that don't require an object be
created, where we can simply call their functions directly:'''

class openclass:
    @staticmethod
    def write(message):
        print message

openclass.write("Hello") #prints 'Hello'
