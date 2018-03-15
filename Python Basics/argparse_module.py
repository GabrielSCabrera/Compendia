import argparse
parser = argparse.ArgumentParser()      #Setting up the parser

metavar = "-a"                          #Hyphen is required, user input var
description = "-argument_a"             #Hyphen is required
var_name = "a"                          #Name of variable, given by parse_args
choose_type = int                       #What type is expected
default_val = 0                         #If var isn't input, its default value
help_text = "help text goes here"       #Text displayed when -h is selected
metavariable = "a"

parser.add_argument(metavar, description, dest = var_name, type = choose_type,
                default = default_val, help = help_text, metavar = metavariable)

user_input = parser.parse_args()

print user_input.a
