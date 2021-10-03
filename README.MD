A more simple and intuitive way of adding arguments to argparse. Will also automatically format a help message that shows default variable names, expected type and wraps lines at the edge of the screen into neat blocks. You can also take full control of the help section and format it better. See more in the [Help](#help) section below, or just run [**example.py**](example.py) to see it in action!

&nbsp;
## Usage:

Instead of trying to remember how to implement and type this mess (and keep it under the line limit):

```
    def msg():
        return "./example.py <pos arg> --options..."

    parser = argparse.ArgumentParser(allow_abbrev=True, usage=msg())
    pos = parser.add_argument_group("Positional Arguments")
    pos.add_argument('pos1', nargs='?', default='', help="Positional argument 1")
    basic = parser.add_argument_group("Optional Arguments")
    basic.add_argument('--name', dest='name', default='', type=str, help="Enter your name")
    basic.add_argument('--age', dest='min_age', nargs='?', type=int, default=365, help="File age in days")
    basic.add_argument('--size', nargs='?', type=float, default=100, help="Min file size in MB\nAs this is a multline help in the source code, the second line has been automatically bumped down. Starting at the word 'As'")
    basic.add_argument('--verbose', '-v', action='store_true', help="Very verbose help")
    basic.add_argument('--three', dest='three', default=[], type=str, nargs=3, help="Three items must follow this argument.")

```

You can just create an array like this:

```
    basic_args = [\

        ['name'],
        "Enter your name",

        ['age', 'min_age', int, 365],
        "File age in days",

        ['verbose', '', bool],
        "List each file deleted",

        ]

```
and get the results with:

```
    return easy_parse(basic_args)
```

&nbsp;
## Format:

The format is simply an array with these lines:

```
    ['alias', 'variable_name', type, 'default_value'],
    "help string",
```

The best part is that everything is optional (including the help line). You can include as many items in the above list as you need or just: `['variable_name']` easy_parse() will interpret the array, fill in any missing sections, allow for abbreviated commands and format a nice help message if the user passes `-h` Don't worry about dashes, by default either '-' or '--' will work automatically.


&nbsp;
## Lists:

Simply use the variable type `list` or a number like `3` to specify the number of required arguments:

```
    ['three', '', 3],
    "Three items must follow this argument."
```

&nbsp;
## Positional args, Hidden args and Subgroups:

For more control you can split up arguments into groups.

For example, if I wanted to add positional arguments:

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

  * To make a subgroup **positional** pass: `positionals=True`
  * To make a subgroup **hidden** pass: `hidden=True`

&nbsp;
## More advanced usage:

Not every feature of ArgumentParser is available automatically yet, but because my class is built on top of ArgumentParser, you can simply add to the parser directly with standard syntax by running commands like `am.parser.add_argument(...)` with whatever features you need. Let me know if you would like to see any new features implemented!

&nbsp;
## Help:

By default, passing `-h` or `--help` will automatically generate a help text that looks something like this.

```
Usage: example.py ./example.py <pos arg> --options...


Positional Arguments:
  pos1 <str>        Positional argument 1.


Optional Arguments:
  --age <int>       File age in days.  Default: 365
  --name <str>      Enter your name.
  --size <float>    Min file size in MB
                    As this is a multline help in the source code, the second line has been
                    automatically bumped down. Starting at the word 'As'  Default: 100
  --three <str>     Three items must follow this argument.
  --verbose         Make everything very verbose. As verbosity is very important to
                    understanding, this is a very verbose help line. As you can see it wraps at
                    the edge of the screen (or the given `wrap` value, whichever is lower), but
                    fear not! It will automatically fit neatly into it's place thanks to the
                    magic in sd/columns.py.

```


**Features**:

  * No more: `--help` showing up under its own optional section.
  * No more: `[DEFAULT_ARGUMENT_NAME]` showing up in help.
  * Newlines in help messages. Just add `\n` to your strings.
  * Automatically shows the help section broken up into subgroups.
  * Automatically shows the expected argument type (if non string)
  * Automatically shows the default value.
  * Automatically wraps text at the edge of the screen or whatever value you like with `am.parse(wrap=???)`
  * Automatically capitalizes first letter and adds a period.



&nbsp;
## Try it out:

A full example of this you can play with is in [**example.py**](example.py)

You can see what each line is doing exactly by passing `verbose=True` to the `ArgMaster` class on initialization.

Want to see it in use in a much larger project with multiple subsections including positional and hidden args? Check out the parse_args() function in [this project](https://github.com/SurpriseDog/KeyLocker/blob/master/args.py)
