#Tuples behave similarly to tuples, and we can extract information using similar
#commands however they cannot be altered in the same way as a tuple

tuple_one = (1,2,3)

n = 2
m = 3

print tuple_one          #This will print the whole tuple in one line
print tuple_one[n]       #This will print element 'n' of the tuple
print tuple_one[-n]      #This will print the n-th to last element in the tuple

len(tuple_one)           #This will return the length of the tuple

tuple_one.index(n)       #This will find the index of element 'n' in the tuple
n in tuple_one           #This will determine whether element 'n' is in the tuple

tuple_two = (4,5,6)

tuple_three = tuple_one + tuple_two   #This will add tuple_two to the end of tuple_one

one, two, three = tuple_one     #These variables will be assigned the values
                                #of the tuple's elements, respectively

#If two tuples have the same number of elements, we can traverse both
#simultaneously using a loop and 'zip' and print them as a table
#with two columns, each representing a separate tuple

for a,b in zip(tuple_one, tuple_two):
    print "%.0f %.0f" %(a,b)
