#To print objects, it is recommended you import pprint and/or scitools
import pprint

list_one = [1,2,3,4,5]
list_two = [6,7,8,9,10]
table_one = [[a,b] for a,b in zip(list_one,list_two)]

pprint.pprint(table_one)    #This will format your table more nicely then print
