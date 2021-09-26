#!/usr/bin/python3
# todo compile easy_args.py with built in functions using wrangler and record how you built it.
# talk about the help formatting with auto_cols
# side by side with default_parsers

import argparse
import easy_args

def my_parser():
	"An example using my custom parser"

	# The class itself
	# newline is the number of newlines between groups
	# verbose prints what each argument looks like with parser.add_argument
	am = easy_args.ArgMaster(usage="./example.py <pos arg> --options...", newline='\n'*2, verbose=True)

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
		"Min file size in MB to be considered 'large'",

		['verbose', '', bool],
		"List each file deleted",

		['three', '', 3],
		"Three items must follow this argument.",
		]
	am.update(basic_args, 'Optional Arguments:')

	return am.parse(wrap=100)


def main():
	#show_args(default_parser())

	print("ArgumentParser arguments:")
	args = my_parser()
	print("#" * 80)

	print("\nArguments passed by user:")
	easy_args.show_args(args)




if __name__ == "__main__":
	main()
