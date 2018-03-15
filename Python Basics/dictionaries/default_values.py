dictionary = {'key_a': 1, 'key_b': 2, 'key_c': 3}

'''To prevent KEYERRORS from occuring, we can set default values,
such that if the key we look up doesn't exist in our dictionary, an
object of our choosing is returned in its place'''

empty_key = dictionary.get('key_d',4) #empty_key will get the value 4

'''If we want to create a dictionary with a default value, we must
import collections.defaultdict'''

from collections import defaultdict

'''The following will first give dictionary2 the default value 0, and
then sets all its pairs equal to those in dictionary'''

dictionary2 = defaultdict(lambda: 0.0)
dictionary2.update(dictionary)

'''Keep in mind that you must use a function, which cannot contain any 
arguments'''

'''If we now try and check for a key that isn't in the dictionary,
not only will we get the value 0 returned, but the new key-value
pair will be added to the dictionary'''
