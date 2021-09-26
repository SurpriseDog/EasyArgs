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

		['three', '', 3],
		"Three items must follow this argument.",
		]
	am.update(basic_args, 'Optional Arguments:')

	return am.parse(wrap=95)


def main():
	print("ArgumentParser arguments:")
	args = my_parser()
	print("#" * 80)

	print("\nArguments passed by user:")
	easy_args.show_args(args)




if __name__ == "__main__":
	main()
