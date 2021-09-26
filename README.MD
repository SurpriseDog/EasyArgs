A more simple and intuitive way of adding arguments to argparse. Will also automatically format a help message that shows default variable names, expected type and wraps lines at the edge of the screen into neat blocks. See more in the Help section below or just run **example.py** to see it in action!

---

### Format:

Instead of trying to remember how to implement and type this mess (and keep it under the line limit):

```
    parser = argparse.ArgumentParser(allow_abbrev=True)
    parser.add_argument('--age', dest='min_age', nargs='?', type=float, default=365, help="File age in days")
    parser.add_argument('--size', args='?', type=float, default=100, help="Min file size in MB.")
    parser.add_argument('--verbose', '-v', action='store_true', help="List each file deleted")
    return parser.parse_args()

```

You can simply create an array like so. The **format** is simply:

```
	['alias', 'variable_name', type, default],
	"help string",
```

The best part is that everything is optional. You can include as many items in the above list as you need or just simply: `['variable_name']`



### Example

```
	basic_args = [\
	['age', 'min_age', int, 365],
	"File age in days",

	['size', '', float, 100],
	"Min file size in MB to be considered 'large'",

	['verbose', '', bool],
	"List each file deleted",
	]
```

Pass it to a single function that will interpret the array, fill in any missing sections, allow for abbreviated commands and format a nice help message if the user passes `-h`

```
	return easy_parse(basic_args)
```

### Lists

Simply use the variable type `list` or a number like `3` to specify the number of required arguments:

```
	['three', '', 3],
	"Three items must follow this argument."
```

### Positional args and Subgroups

For more control you can split up arguments into groups. For example If I wanted to add positional arguments:

```
	pos_args = [\
	['pos1'],
	"Positional argument 1",
	['pos2'],
	"Positional argument 2",
	]
```

Then you can combine all of the subgroups together with the full `ArgMaster` class like so:

```
	am = ArgMaster(usage="...")
	am.update(pos_args, 'Positional Arguments:', positionals=True)
	am.update(basic_args, 'Optional Arguments:')
	return am.parse()
```

### More advanced usage

Not every feature of ArgumentParser is available automatically, but because my class is built on top of ArgumentParser, you can simply add to the parser directly with standard syntax by running commands like `am.parser.add_argument(...)` with whatever features you need.

Let me know if you would like to see any new features implemented!


### Help

### Try it out:

A full example of this you can play with is in **example.py**
You can see what each line is doing exactly by passing `verbose=True` to the `ArgMaster` class.
