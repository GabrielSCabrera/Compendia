#We can allow a program to branch into several different ways by using
#if statements.  We can combine several at a time using "and" & "or":

condition = True

if condition == True:
    print "Condition is True"

if condition == False:
    print "Condition is False"

if condition != True and condition != False:
    print "There exists no condition"

#This can be rewritten more compactly by using Else and Elif statements

condition = True

if condition == True:
    print "Condition is True"
elif condition == False:
    print "Condition is False"
else:
    print "There is no condition"

#We can also compare numbers -- see "boolean_values.py" for more info.
#Here is an example where we check if our number is greater than 0

number = 2

if number > 0:
    print "Number is greater than zero"
else:
    print "Number is not greater than zero"

#We can also shorten a simple if-statement using an "inline if test":

if condition == True:
    result = True
else:
    result = False

#This can be shortened to the following:

result = (True if condition == True else False)

#Inline if tests can be used in lambda functions!
