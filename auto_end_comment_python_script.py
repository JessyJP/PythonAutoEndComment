"""
auto_end_comment_python_script.py

Date: 23-04-2023
Author: JessyJP (my_@gmail.com)
License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License

Description:
This script takes one or more Python files as input and automatically adds '#end' comments to the end of code blocks such as if statements, loops, and functions. It helps improve code readability by clearly marking the end of each block. The script processes each file and inserts the '#end' comments while maintaining existing comments and empty lines between code blocks.

Usage:
python auto_end_comment_python_script.py <file1> [<file2> ...]

"""

# Improt
import sys
import os
import re

# Strip existing end comments from the code that are alone on a line
def strip_existing_end_comments(code):
    lines = code.split('\n')
    stripped_lines = []
    end_comment_pattern = re.compile(r'^\s*#end\s*$')

    for line in lines:
        if not end_comment_pattern.match(line):
            stripped_lines.append(line)
        #end
    #end

    return '\n'.join(stripped_lines)
#end

# Check if the given line starts a new block
def is_block_start(line):
    return any(
        line.lstrip().startswith(keyword)
        for keyword in ("def ", "class ", "if ", "while ", "for ", "try:", "with ")
    )
#end

# Check if the given line contains code and is not a comment
def is_code_line(line):
    multiline_comment_pattern = re.compile(r"('''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\")")
    stripped_line = line.lstrip()
    return stripped_line and not (stripped_line.startswith("#") or multiline_comment_pattern.match(stripped_line))
#end

def find_next_non_empty_line(lines, start_idx):
    for idx in range(start_idx + 1, len(lines)):
        if is_code_line(lines[idx]):
            return idx
        #end
    #end
    return -1
#end

def print_tree_structure(depth, line_number, keyword, block_type):
    if verbose_output_enabled:
        indent = "|----" * depth
        print(f"{indent} Line {line_number + 1}: {keyword} ({block_type})")
    #end
#end

# Find all the code blocks in the given lines
def find_blocks(lines):
    blocks = []
    indent_levels = []
    block_starts = []

    # Keywords that start a new block
    start_keywords = ("def ", "class ", "if ", "elif ", "else:", "while ", "for ", "try:", "except ", "finally:", "with ")
    # Keywords that can continue a block
    continuation_keywords = {
        "if": ("elif", "else:"),
        "elif": ("elif", "else:"),
        "try:": ("except", "finally:"),
        "except": ("except", "finally:"),
    }

    last_opened_keyword = []
    next_line_stripped = None

    for line_idx, line in enumerate(lines):
        if not is_code_line(line):
            continue
        #end

        stripped_line = line.lstrip()
        current_indent = len(line) - len(stripped_line)

        if not indent_levels and current_indent == 0 and not any(stripped_line.startswith(keyword) for keyword in start_keywords):
            if verbose_output_enabled:
                print(f"Line {line_idx + 1}: No indentation and no keyword, ignoring")
            #end
            continue
        #end

        def checkForContinuation():
            skipLine = False
            # Check if the given line is a continuation of a block
            if len(last_opened_keyword)>0 and stripped_line:
                continuation = continuation_keywords.get(last_opened_keyword[-1], ())
                for keyword in continuation:
                    if stripped_line.startswith(keyword) and current_indent == indent_levels[-1]:
                        skipLine = True
                        last_opened_keyword.pop()
                        last_opened_keyword.append(keyword)
                        print_tree_structure(len(indent_levels)-1, line_idx, keyword, "Block Continuation")
                        break
                    #end
                #end
            #end
            return skipLine
        #end
        if checkForContinuation(): 
            continue
        #end

        while indent_levels and current_indent <= indent_levels[-1]:
            last_opened_keyword.pop()
            indent_levels.pop()
            block_start = block_starts.pop()
            next_non_empty_line = find_next_non_empty_line(lines, block_start[0])
            if block_start and next_non_empty_line != -1:
                next_line_stripped = lines[next_non_empty_line].lstrip()
                blocks.append((block_start, line_idx - 1))
                print_tree_structure(len(indent_levels), line_idx - 1, block_start[2], "Block End")
            #end
            if checkForContinuation(): 
                break
            #end
        #end

        if is_block_start(stripped_line):
            indent_levels.append(current_indent)
            open_keyword = stripped_line.split()[0]
            block_starts.append((line_idx, current_indent, open_keyword))
            print_tree_structure(len(indent_levels) - 1, line_idx, open_keyword, "Block Start")
            last_opened_keyword.append(open_keyword)# Keeps track of depth
        #end
    #end

    while indent_levels:
        indent_levels.pop()
        block_start = block_starts.pop()
        next_non_empty_line = find_next_non_empty_line(lines, block_start[0])
        if block_start and next_non_empty_line != -1:
            next_line_stripped = lines[next_non_empty_line].lstrip()
            blocks.append((block_start, len(lines) - 1))
            print_tree_structure(len(indent_levels), len(lines) - 1, block_start[2], "Block End")
        #end
    #end

    return blocks
#end


# Find the index of the last code line before the end of the block
def find_last_code_line(lines, end):
    while end >= 0 and not is_code_line(lines[end]):
        end -= 1
    #end
    return end
#end

# Add end comments to the given code
def add_end_comments(code):
    stripped_code = strip_existing_end_comments(code)
    lines = stripped_code.split('\n')
    blocks = find_blocks(lines)

    for start, end in reversed(blocks):
        start_line = lines[start[0]]
        last_code_line = find_last_code_line(lines, end)
        if not lines[last_code_line].rstrip().endswith("#end"):
            indent = ' ' * start[1]
            lines.insert(last_code_line + 1, f"{indent}#end")
        elif start[1] != len(lines[last_code_line]) - len(lines[last_code_line].lstrip()) - 4:
            lines[last_code_line] = ' ' * start[1] + '#end'
        #end
    #end

    return '\n'.join(lines)
#end

# Process the input files and add end comments
def process_files(input_files, output_suffix=''):
    for input_file in input_files:
        with open(input_file, 'r') as file:
            code = file.read()
        #end

        modified_code = add_end_comments(code)

        output_file = os.path.splitext(input_file)[0] + output_suffix + os.path.splitext(input_file)[1]
        with open(output_file, 'w') as file:
            file.write(modified_code)
        #end

        print(f"Processed {input_file} -> {output_file}")
    #end
#end

# ===========================================================================================
import argparse
from pathlib import Path

# Global variable for verbose output
verbose_output_enabled = False

def process_directory(directory, recursive=False):
    file_list = []
    for ext in ["*.py"]:
        if recursive:
            file_list.extend(list(directory.glob(f"**/{ext}")))
        else:
            file_list.extend(list(directory.glob(ext)))
        #end
    #end
    return file_list
#end

def parse_args():
    parser = argparse.ArgumentParser(description='Automatically add end comments to Python code blocks')
    parser.add_argument('input', type=str, nargs='+', help='List of files or directories to process')
    parser.add_argument('-r', '--recursive', action='store_true', help='Process subdirectories recursively when a directory is provided')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose diagnostic output')
    return parser.parse_args()
#end

# Main function
if __name__ == '__main__':
    args = parse_args()
    verbose_output_enabled = args.verbose
    input_items = [Path(item) for item in args.input]
    input_files = []

    for item in input_items:
        if item.is_file() and item.suffix == '.py':
            input_files.append(str(item))
        elif item.is_dir():
            input_files.extend([str(file) for file in process_directory(item, args.recursive)])
        else:
            print(f"Invalid input: {item}, skipping")
        #end
    #end
    
    if not input_files:
        print("No valid .py files found to process")
        sys.exit(1)
    else:
        process_files(input_files)
    #end
#end

