'''Variables created inside a function are local -- that is to say,
they cannot be accessed outside the function, whereas global variables can
be accessed both inside and outside all functions.'''

global_variable = 0

def test_function():
    global_variable = 10
    local_variable = 10

test_function()

print global_variable           #The function successfully set this to 10
print local_variable            #This variable doesn't exist outside the
                                #function and has the value NaN
