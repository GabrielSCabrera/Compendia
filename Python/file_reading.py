permissions = "r"       #Determines what you can do with the open
                        #file, 'r' for reading & 'w' for writing
                        #and 'a' for appending

file_path = "data.txt"  #Gives the file name and location

file_object = open(file_path, permissions)

lines = file_object.readlines()
#This is equivalent to the following:

lines = [line for line in file_object]
#Which is also equivalent to the following:

lines = []                  #Here we are reading the open file
for line in file_object:    #line by line and appending it into
    lines.append(line)      #a list

file_object.close()     #IMPORTANT - always close your file after
                        #you are done using it

#We can also open, use, and close a file using "with open":

with open(file_path, permissions) as file_object:
    pass

#For more organized formatting, save the file data to a string:

with open(file_path, permissions) as file_object:
    file_string = file_object.read()

#Here we are taking the sum of all the integers in our file; we
#have to make sure we don't try adding strings, so we make use of
#try/except and convert the number strings to integers

with open(file_path, permissions) as file_object:
    int_sum = 0
    for line in file_object:
        try:
            int_sum += int(line)
        except:
            pass

#Our data file contains 3 lines with two words each, we can extract
#individual words and save them, for example, to a list like so:

with open(file_path, permissions) as file_object:
    word_list = [[],[]]
    for line in file_object:
        try:
            int(line)
        except:
            temp_word = line.split()
            word_list[0].append(temp_word[0])
            word_list[1].append(temp_word[1])

print word_list
