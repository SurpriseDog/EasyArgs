#!/usr/bin/python3
# An example usage of easy_args
# Want to see it in use in a much LARGER project with multiple subsections including positional and HIDDEN args?
# Check out the parse_args() function in:
# https://github.com/SurpriseDog/KeyLocker/blob/master/args.py

import argparse
import easy_args

def my_parser():
	"An example using my custom parser"

	# The class itself
	# newline is the number of newlines between groups
	# verbose prints what each argument looks like with parser.add_argument
	am = easy_args.ArgMaster(usage="./example.py <pos arg> --options...",
							 newline='\n'*2,
							 exit=False,
							 verbose=True)

	# A list of required Positional arguments:
	pos_args = [\
		['pos1'],
		"Positional argument 1",
		]
	am.update(pos_args, 'Positional Arguments:', positionals=True)


	# A list of Optional arguments
	basic_args = [\
		['name'],
		"Enter your name",

		['age', 'min_age', int, 365],
		"File age in days",

		['size', '', float, 100],
		'''
		Min file size in MB
		As this is a multline help in the source code, the second line has been automatically bumped down. Starting at the word 'As'
		''',

		['verbose', '', bool],
		'''Make everything very verbose. As verbosity is very important to understanding this is a very verbose help line. As you can see it wraps at the edge of the screen (or the given `wrap` value, whichever is lower), but fear not! It will automatically fit neatly into it's place thanks to the magic in sd/columns.py''',

		['three', None, 3],
		"Three items must follow this argument.",
		]
	am.update(basic_args, 'Optional Arguments:')

	return am.parse(wrap=95)

def old_parser():
	"An example of the above using the default argparse syntax"

	def msg():
		return "./example.py <pos arg> --options..."

	parser = argparse.ArgumentParser(allow_abbrev=True, usage=msg())

	pos = parser.add_argument_group("Positional Arguments")
	pos.add_argument('pos1', nargs='?', default='', help="Positional argument 1")

	basic = parser.add_argument_group("Optional Arguments")
	basic.add_argument('--name', dest='name', default='', type=str, help="Enter your name")
	basic.add_argument('--age', dest='min_age', nargs='?', type=int, default=365, help="File age in days")
	basic.add_argument('--size', nargs='?', type=float, default=100, help="Min file size in MB\nAs this is a multline help in the source code, the second line has been automatically bumped down. Starting at the word 'As'")
	basic.add_argument('--verbose', '-v', action='store_true', help="List each file deleted")
	basic.add_argument('--three', dest='three', default=[], type=str, nargs=3, help="Three items must follow this argument.")

	return parser.parse_args()




def main():

	args = my_parser()
	print("#" * 80)

	print("\nDefault argparse syntax for reference:\n")
	easy_args.show_args(old_parser())

	if args:
		print("\nEasyArgs passed by user:\n")
		easy_args.show_args(args)



if __name__ == "__main__":
	main()
