'''Basics'''

string = "abcdefg"

c = string[2]       #returns c

cdef = string[2:6]  #returns cdef

abcdef = string[:6] #returns abcdef

defg = string[3:]   #returns defg

abc = string[0:-4]  #returns abc

'''Substring Positions:'''

position_of_f = string.find('f')    #returns 5

position_of_fg = string.find('fg')  #returns 5

'''Checking for substrings:'''

contains_h = 'h' in string                  #returns False

starts_with_abc = string.startswith('abc')  #returns True

ends_with_efg = string.endswith('efg')      #returns True

'''Substitution:'''

string = string.replace('g','hh') #replaces all 'g' with 'hh'
#String becomes 'abcdefhh'

string = string.replace('h','g',1) #replaces the first 'h' with 'g'
#String becomes 'abcdefgh'

'''Splitting:'''

#Let's first divide the letters in our string with commas
string = "a,b,c,d,e,f,g,h"
#We can then split these into list elements, divided along the commas
str_list = string.split(',')
#This outputs ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#If a string contains a number of \n, we can split it with splitlines:
string = "a\nb\nc\nd\ne\nf\ng\nh"
str_lines = string.splitlines()

'''Joining:'''

string = ''.join(str_list)  #joins all elements of str_list, with
                            #the character '' in between

'''Extending:'''
string += "ijk" #returns 'abcdefghijk'
print  string

'''Upper and Lower Case:'''

all_uppercase = string.upper()  #returns ABCDEFGH
all_lowercase = string.lower()  #returns abcdefgh

'''Testing for digits:'''

contains_only_digits = string.isdigit() #returns False

'''Testing for Whitespace (' ', '\n', '\t'):'''

string_is_empty = string.isspace()  #returns False

print all_uppercase

'''Stripping a string:'''
string = '   abcdefghi   '
string = string.strip() #returns 'abcdefghi'
