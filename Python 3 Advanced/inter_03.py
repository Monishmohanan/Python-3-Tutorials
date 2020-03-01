# Python Argparse library

import argparse
import os
import sys

# create the parser
my_parser = argparse.ArgumentParser(description = 'List the contents of the folder')

# add the arguments
my_parser.add_argument('Path', metavar = 'path', type = str, help='path to the list')

# execute the parse_args() method
# we have executed .parse_args() 
# to parse the input arguments and get a Namespace object that contains the user input.
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
	print("the path specified does not exist")
	sys.exit()

print("\n".join(os.listdir(input_path)))