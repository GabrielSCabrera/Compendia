'''To store a set of values we can use a simple list, but it's also
possible to create a dictionary with indices (which we call keys)
paired to each value in the dictionary, such that we can extract
specific values using their respective keys.
'''

'''The following are two means to the same end'''

dictionary = {'key_a': 1, 'key_b': 2, 'key_c': 3}

dictionary = dict(key_a=1, key_b=2, key_c=3)

'''The following will add a new value to our dictionary'''

dictionary['key_d'] = 4

'''We can extract a specific value using its key'''

value = dictionary['key_a']

'''We can use a 'x in y' type statement to parse through our values,
and use sorted(y) to alphabetize the order, otherwise the order
will not be predictable, like in a list'''

for key in dictionary:                          #Unpredictable Order
    print "%s: %s" %(key,dictionary[key])

for key in sorted(dictionary):                  #Alphabetized Order
    print "%s: %s" %(key,dictionary[key])

'''We can find out whether a dictionary contains a key, as a Boolean'''

key_in_list1= 'key_e' in dictionary #Would be False
key_in_list2= 'key_a' in dictionary #Would be True

'''We can extract all keys, or all values, as lists'''

all_keys = dictionary.keys()
all_vals = dictionary.values()

'''We can delete a particular value like so:'''

del dictionary['key_d']

'''IMPORTANT NOTE - if you set a new variable equal to an already
existing dictionary, changing a variable in either dictionary will
affect the other, seeing as they are both considered one and the same.
To avoid this problem, one must use the copy command as follows:'''

dictionary_copy = dictionary.copy()

'''We can combine dictionaries by using the update function'''

dictionary2 = {'key_d': 4}
dictionary2.update(dictionary)
