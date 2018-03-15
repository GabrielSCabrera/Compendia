#We can define a function as follows:

def function_name(argument_one, argument_two = 0):  #Parameters are optional

    """It is standard to describe your function with a "Doc String"
    right after the function declaration, within triple quotes,
    since a function can do pretty much anything you need it to,
    a description is often necessary when dealing with large programs"""

    #argument_one must be defined when the function is called, but
    #argument_two can be left blank and would - in that case - be
    #given the value defined above ['0' in this case]

    #We can use the arguments within our function now

    result_one = argument_two
    result_two = argument_one

    return result_one, result_two   #Returning data is optional in a function

#You can get the doc string by using the command

docstring = function_name.__doc__

#If you are using an imported module, make sure to put the name of the module
#before the command, separated by a '.'

#Remember!  Variables created inside a function are local -- that is to say,
#they cannot be accessed outside the function, whereas global variables can
#be accessed both inside and outside all functions.

#To call the function we must keep it's parameters in mind

function_input = 5

value_one, value_two = function_name(function_input, 0)
tuple_one = function_name(function_input, 0)

#The function's input has now been interpreted by the function as its
#parameters, and the 'value_n' variables will save the data returned
#as two separate variables -- tuple_one however stores the returned
#data as a single tuple

print value_one, value_two         #These will print what the function returns
print tuple_one                    #as two different types - int and tuple

#It is also possible to have default

"""Remember -- calling a function means you are using whatever it returns, so
if you use a function as an argument it will take the value of whatever it
returns!"""
