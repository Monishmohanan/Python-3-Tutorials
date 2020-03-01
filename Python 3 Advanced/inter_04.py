import argparse
import sys
import os

# Additional options in argparse

# SETTING THE NAME OF THE PROGRAM
my_parser = argparse.ArgumentParser(prog = 'myls',
	description = 'List the contents of the folder')

# DISPLAYING A CUSTOM PROGRAM USAGE HELP
my_parser = argparse.ArgumentParser(prog='myls',
	usage = '%(prog)s [options] path',
	description = 'Lists the contents of the folder')

# DISPLAYING TEXTS BEFORE AND AFTER THE ARGUMENTS HELP
# description: for the text that is shown before the help text
# epilog: for the text that is shown after the help text
my_parser = argparse.ArgumentParser(description = 'Lists the contents of the folder',
	epilog = 'Enjoy the program!')

# CUSTOMIZING THE ALLOWED PREFIX CHARACTER
# standard prefix char is the dash(-) character
my_parser = argparse.ArgumentParser(description = 'Lists the contents of the folder',
	epilog = 'Enjoy the program!',
	prefix_chars = '/')
# now the program supports /h flag instead of -h flag

#