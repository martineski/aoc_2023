#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

"""Brief description of the script."""

# Other imports or code ...
import sys
import re

# Constants
RED_MAX     = 12
GREEN_MAX   = 13
BLUE_MAX    = 14

# Classes

# Functions
def solverPart1(file_path):

    tot_id_games = 0

    with open(file_path, 'r') as f:
        for line in f:
            matches = re.findall(r"(\d+) ([r|g|b])", line)
            id = re.findall(r"Game (\d+):", line)

            num_ok = 0
            if matches:
                for m in matches:
                    val = int(m[0])
                    color = m[1]
                    if (color == 'r' and val <= RED_MAX):
                        num_ok += 1
                    elif (color == 'g' and val <= GREEN_MAX):
                        num_ok += 1
                    elif (color == 'b' and val <= BLUE_MAX):
                        num_ok += 1

            if num_ok == len(matches):
                tot_id_games += int(id[0])

    return tot_id_games

def solverPart2(file_path):

    tot_powers_rgb = []

    with open(file_path, 'r') as f:
        for line in f:
            matches = re.findall(r"(\d+) ([r|g|b])", line)

            if matches:
                min_cubes = { 'red': 0, 'green': 0, 'blue': 0 }
                for m in matches:
                    val = int(m[0])
                    color = m[1]
                    if (color == 'b' and min_cubes['blue'] < val):
                        min_cubes['blue'] = val
                    elif (color == 'r' and min_cubes['red'] < val):
                        min_cubes['red'] = val
                    elif (color == 'g' and min_cubes['green'] < val):
                        min_cubes['green'] = val


                game_powers_rgb = 1
                for v in min_cubes.values():
                    game_powers_rgb *= v

                tot_powers_rgb.append(game_powers_rgb)

    return sum(tot_powers_rgb)


def main(argument):
    """Main function."""
    # Your code here that uses the 'argument' parameter
    print("Argument received:", argument)

    res = solverPart1( argument )
    print("====> TOT ID GAMES:", res)

    res = solverPart2( argument )
    print("====> TOT POWS:", res)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solver.py <argument>")
        sys.exit(1)

    argument_value = sys.argv[1]  # Get the argument from the command line
    main(argument_value)  # Call the 'main' function with the argument
