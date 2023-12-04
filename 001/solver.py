#!/usr/bin/env python3.10.12
# -*- coding: utf-8 -*-

"""Brief description of the script."""

# Module imports
import re
import sys
import pdb

# Constants
# dictionary for part 2 of the challenge
text_to_number = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# Classes

# Functions
def inputReaderPart1(file_path):
    res = 0

    with open(file_path, 'r') as f:
        for line in f:
            print(line.strip())
            numbers_only = re.findall(r'\d', line)
            print(numbers_only)

            tmp = 0
            if ( len(numbers_only) >= 1 ):
                tmp = int(numbers_only[0] + numbers_only[-1])
                # in case of only one number found, it gets duplicated

            res += tmp
            print(tmp)

    print('====> ' + str(res))

def inputReaderPart2(file_path):
    res = 0

    with open(file_path, 'r') as f:
        first = -1
        last = -1
        for line in f:
            line = line.strip()

            # find all words and numbers in the line
            words_numbers = re.findall(r'[a-zA-Z]+|\d', line)
            print(words_numbers)

            # convert textual representations to numeric values
            output = []
            for word in words_numbers:
                fs, ls = getValidSubstrings(word)

                if (first == -1 and fs != -1):
                    first = fs
                if (last != -1 and ls != -1):
                    last = ls
                elif (first != -1 and fs != -1):
                    last = fs

            # special case: only one item was found in the whole string
            # if so, repeat the value (e.g. '3' -> '33')
            if (last == -1):
                last = first

            # skip lines that have no valid number in them
            if (first != -1 and last != -1):
                line_result = int(str(first) + str(last))
                print("COMB:", line_result)
                res += line_result
                print("TOT:", res)

            first = last = -1
            print("===")

    print("res: ", res)

def getValidSubstrings(input_string):
    length = len(input_string)
    valid_substrings = []

    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = input_string[i:j]
            if substring in text_to_number:
                valid_substrings.append(text_to_number[substring])
            elif re.findall(r'\d', substring):
                valid_substrings.append(substring)

    first = last = -1

    if len(valid_substrings) != 0:
        first = valid_substrings.pop( 0 )
    if len(valid_substrings) != 0:
        last = valid_substrings.pop( -1 )

    return first, last


def main(args):
    """Main function."""
    if args == 'sample1':
        inputReaderPart1('sample1')
    if args == 'sample2':
        inputReaderPart2('sample2')
    elif args == 'input1':
        inputReaderPart1('input')
    elif args == 'input2':
        inputReaderPart2('input')
    elif args == 'tst':
        inputReaderPart2('tst')
    else:
        print("Invalid argument. Please provide either 'sample1', 'sample2' or 'input1', 'input2'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solver.py <argument>")
        sys.exit(1)

    main(sys.argv[1])
