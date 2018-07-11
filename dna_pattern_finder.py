#!/usr/bin/env python

import sys
import os
import re

# Getting parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if len(sys.argv) < 2:
    print("You need to give a text file with the DNA sequence inside.")
    exit(0)

path_file = sys.argv[1]
if not os.path.isfile(path_file):
    print("File not valid. You need to give a text file with the DNA sequence inside.")
    exit(0)

current_arg_nb = 2
if len(sys.argv) > current_arg_nb:
    if sys.argv[current_arg_nb] not in ["1", "0"]:
        print("You need to give a good boolean value to now if there is an output of not.")
        exit(0)
    if sys.argv[current_arg_nb] == "1":
        rapport_path = "rapport.txt"
    else:
        rapport_path = os.devnull
else:
    rapport_path = os.devnull


current_arg_nb += 1
if len(sys.argv) > current_arg_nb:
    if not bool(re.search('^[GTAC]*$', sys.argv[current_arg_nb])):
        print("You need to give a good pattern, with only G, T, A or C.")
        exit(0)
    pattern = sys.argv[current_arg_nb]
else:
    pattern = "GG"

current_arg_nb += 1
if len(sys.argv) > current_arg_nb:
    if not int(float(sys.argv[current_arg_nb])) >= 1:
        print("You need to give a good 'size before - min' battern, at least 1.")
        exit(0)
    size_before_min = int(float(sys.argv[current_arg_nb]))
else:
    size_before_min = 2

current_arg_nb += 1
if len(sys.argv) > current_arg_nb:
    if not int(float(sys.argv[current_arg_nb])) >= 1:
        print("You need to give a good 'size before - max' battern, at least 1.")
        exit(0)
    size_before_max = int(float(sys.argv[current_arg_nb]))
else:
    size_before_max = 10


# We get the content of the file
with open(path_file, 'r') as adn_file:
    dna = adn_file.read().replace("\n", "")

with open(rapport_path, 'w') as rapport_file:
    # For each value of the loop
    for size_before in range(size_before_min, size_before_max+1):
        # We reset the res
        res = {}
        place = size_before

        while place != -1:
            place += 2
            place = dna.find(pattern, place)

            if place == -1:
                continue
            str_before = dna[place-size_before:place+len(pattern)]
            if str_before in res:
                res[str_before] += 1
            else:
                res[str_before] = 1
        print("Ordered result for " + str(size_before) + " characters before the pattern.")
        print(sorted(res.items(), key=lambda kv: kv[1], reverse=True))
        print("\n")
