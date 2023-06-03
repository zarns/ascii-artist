import os
import json
import argparse

with open('fonts/font1.json', 'r') as f:
    char_map = json.load(f)

def string_to_lines(s):
    # Initialize a list of lines with empty strings
    lines = ['' for _ in range(6)]

    # Iterate over the characters in the string
    for char in s:
        # Look up the larger representation of the character
        char_lines = char_map[char]

        # Append the lines of the larger representation to the lines list
        for i in range(6):
            lines[i] += char_lines[i]

    return lines

def write_string_to_file(str1):
    # Convert the string to lines
    lines = string_to_lines(str1)

    # Create a filename based on the first five characters of the input string
    filename = 'text_output/' + str1[:5] + '.txt'

    # Create the output_txt directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Open the file
    with open(filename, 'w') as f:
        # Write the lines to the file
        for line in lines:
            f.write(line + '\n')

import os

def main():
    parser = argparse.ArgumentParser(description='Convert a string to ASCII art.')
    parser.add_argument('input_str', nargs='?', help='The string to convert to ASCII art.')
    args = parser.parse_args()
    if args.input_str:
        input_str = args.input_str
    else:
        input_str = input('Enter a string: ')

    write_string_to_file(input_str)

if __name__ == '__main__':
    main()