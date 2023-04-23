# Add End Comments to Python Files

This Python script takes one or more Python files as input and adds `#end` comments to the end of code blocks such as if statements, loops, and functions.

## Requirements

- Python 3.6 or higher

## Usage

Run the script from the command line, providing one or more input file paths as arguments:

```sh
python auto_end_comment_python_script.py <file1> [<file2> ...]
```


## TODO
[ ] Improve multi-depth continuation. Currently it's keeping track of only one level. 
Because the last keyword gets overwritten by the time the block closes.
Maybe keep one continuation keyword per level.