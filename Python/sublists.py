#We can extract parts of a list structure (slices/sublists) with some of
#the following commands:

n = 1
m = 5

list_one = [0,1,2,3,4,5,6,7,8,9]
print list_one[n:]      #This will print the list, starting at index n
print list_one[n:m]     #This will print the list, from index n to m-1
print list_one[:m]      #This will print the list, ending at index m-1

m = 3

list_two = [[1,2,3],[4,5,6],[7,8,9]]
print list_two[n:m]      #This will print the sublists in list_two,
                         #from sublist index n to m-1
