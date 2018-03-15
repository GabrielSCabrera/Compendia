import sys

a = raw_input('a: ')    #Sets variable a to whatever user inputs, and always
                        #sets it to a 'string' type

b = input('b: ')        #Instead of a string, can return an int or
                        #float if appropriate

c = sys.stdin.readline()    #This is equivalent to raw_input, without a prompt

#We can enter an argument straight from the command line as well in the form:
#   $python input.py argument

argument = sys.argv[1]

#We can take a variable number of inputs with a loop:

argument_list = []

for arg in sys.argv[1:]:
    argument_list.append(arg)
