'''To create ordered dictionaries, we must import the following:'''

from collections import OrderedDict

'''We can order our dictionary by using OrderedDict, since it will
set our dictionary's order equal to the order in which its keys are
registered - note that we must use tuples for this to work'''

di = OrderedDict([('first',1),('second',2),('third',3),('fourth',4)])

'''A for loop will now print these values in the order we defined:'''

for i in di:
    print i, di[i]

'''This gives the output:

first 1
second 2
third 3
fourth 4'''
