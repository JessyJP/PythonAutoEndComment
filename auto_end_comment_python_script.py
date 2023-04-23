"""
add_end_comments.py

Date: 23-04-2023
Author: Your Name (you@example.com)
License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License

This script takes one or more Python files as input and adds '#end' comments to the end of code blocks such as if statements, loops, and functions.
"""

# Improt
import sys
import os
import re

# Check if the given line starts a new block
def is_block_start(line):
    return any(
        line.lstrip().startswith(keyword)
        for keyword in ("def ", "if ", "elif ", "else:", "while ", "for ", "try:", "except ", "finally:", "with ")
    )
#end

# Check if the given line contains code and is not a comment
def is_code_line(line):
    multiline_comment_pattern = re.compile(r"('''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\")")
    stripped_line = line.lstrip()
    return stripped_line and not (stripped_line.startswith("#") or multiline_comment_pattern.match(stripped_line))
#end

# Find all the code blocks in the given lines
def find_blocks(lines):
    blocks = []
    indent_levels = []
    block_starts = []

    for line_idx, line in enumerate(lines):
        if not is_code_line(line):
            continue
        #end

        stripped_line = line.lstrip()
        current_indent = len(line) - len(stripped_line)

        while indent_levels and current_indent <= indent_levels[-1]:
            indent_levels.pop()
            block_start = block_starts.pop()
            if block_start:
                blocks.append((block_start, line_idx - 1))
            #end
        #end

        indent_levels.append(current_indent)
        block_starts.append((line_idx, current_indent) if is_block_start(stripped_line) else None)
    #end

    while indent_levels:
        indent_levels.pop()
        block_start = block_starts.pop()
        if block_start:
            blocks.append((block_start, len(lines) - 1))
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
    lines = code.split('\n')
    blocks = find_blocks(lines)

    for start, end in reversed(blocks):
        start_line = lines[start[0]]
        last_code_line = find_last_code_line(lines, end)
        if not lines[last_code_line].rstrip().endswith("#end"):
            indent = ' ' * start[1]
            lines.insert(last_code_line + 1, f"{indent}#end")
        #end
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


# Main function
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python add_end_comments.py <file1> [<file2> ...]")
        sys.exit(1)
    #end

    input_files = sys.argv[1:]
    process_files(input_files)
#end

