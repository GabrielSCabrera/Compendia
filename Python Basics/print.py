# Various ways one could print text"

import sys

string = "Line One"
num = 3

print string

print "Line Two"

print "Line %.0f, %.3f" %(num, ((float(num)+1)**2)/3.1526)

print """Line Four
Line Five """

print "Line",               #Comma prevents moving to next line
print "Six"

str_2 = "Line "
str_3 = "Seven"

print str_2 + str_3         #We can add strings together, this is called
                            #"string concatenation"

sys.stdout.write("Line Eight\n")    #This is equivalent to print
