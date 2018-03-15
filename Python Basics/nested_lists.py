#We can create a list with rows and columns (aka a matrix) either by
#defining it manually, with a loop, or a list comprehension

n = 0
m = 0

table_one = [[1,2,3],[4,5,6],[7,8,9]]   #Three rows and three columns

print table_one     #Everything will be printed on one line, but separated with
                    #brackets, organized by row

print table_one[0]  #This will print out the first sublist in table_one
print table_one[1]  #This will print out the second sublist in table_one
print table_one[2]  #This will print out the third sublist in table_one

#So remember to begin counting at zero, not one

#The following will print out the element in row n, column m
print table_one[n][m]

#We can also combine two lists into a table
list_one = [0 + 1*i for i in range(10)]     #We start by creating two lists
list_two = [10 + 1*i for i in range(10)]

table_two = [list_one,list_two]     #Now we have a two rowed table

table_three = []                    #Now we have a two columned table.
for a,b in zip(list_one, list_two): #We could have also used a list
    table_three.append([a,b])       #comprehension, as follows:

table_four = [[a,b] for a,b in zip(list_one, list_two)]
