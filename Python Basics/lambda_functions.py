#Lambda functions are basically more compact, but limited, functions
#take the following function as an example:

variable = 2

def large_function(argument):
    return argument**2

result_one = large_function(variable)

print result_one

#This can be rewritten and shortened in the following way:

variable = 2

result = (lambda argument: argument**2)(variable)

print result

#Keep in mind that leaving out the last section "(variable)" will define
#'result' as being a function in and of itself, not a returned value

#Note: you can use inline if tests within a lambda function as follows:

result = (lambda argument: argument**2 if argument > 0 else 0)(variable)
