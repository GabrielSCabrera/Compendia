first_element = 1
increment = 1
final_index = 10

list_one = []

#You can use a list comprehension to easily create a list, instead of a loop
list_one = [first_element + increment*i for i in range(final_index)]
