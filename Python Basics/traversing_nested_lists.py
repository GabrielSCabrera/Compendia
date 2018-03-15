#We can traverse nested lists in two ways:

list_one = [[1,2,3],[4,5,6],[7,8,9]]

#Method one:

for i in range(len(list_one)):
    for j in range(len(list_one[i])):
        print list_one[i][j]

#Method two:

for i in list_one:
    for j in i:
        print j

#Both of these loops will parse through each element of the list
