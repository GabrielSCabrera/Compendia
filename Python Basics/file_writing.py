file_path = "data.txt"
permissions = "w"           #We are allowing our program to overwrite
                            #our open file by using 'w'

save_to_file = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\nLine One\nLine Two\nLine Three\n11\n12\n13"
#This is the string we will write to our file, note the \n will
#create new lines within our file

with open(file_path, permissions) as file_object:
    file_object.write(save_to_file)
