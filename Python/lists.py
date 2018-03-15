list_one = [0,1,2,3,4,5,6,7,8]

n = 8

print list_one          #This will print the whole list in one line
print list_one[n]       #This will print element 'n' of the list
print list_one[-n]      #This will print the n-th to last element in the list

del list_one[n]         #This will remove element 'n' from the list
len(list_one)           #This will return the length of the list

m = 9

list_one.append(n)      #This will add element 'n' to the end of the list
list_one.insert(n,m)    #This will insert element 'm' into position 'n'

list_one.index(n)       #This will find the index of element 'n' in the list
n in list_one           #This will determine whether element 'n' is in the list

list_two = [10,11,12,13,14,15,16,17,18,19]

list_three = list_one + list_two    #This will add list_two to the end of list_one

list_four = [1,2,3]

one, two, three = list_four         #These variables will be assigned the values
                                    #of the list's elements, respectively

list_length = len(list_one)         #Returns number of element in list

#If two lists have the same number of elements, we can traverse both
#simultaneously using a loop and 'zip' and print them as a table
#with two columns, each representing a separate list

for a,b in zip(list_one, list_two):
    print "%.0f %.0f" %(a,b)
