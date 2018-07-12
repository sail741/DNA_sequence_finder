#!/usr/bin/env python

"""

This application look into a file that contains DNA sequence (GCGCGTACG...) to find a pattern, and compare the prefix
of the pattern.
Actually, the application is run multiple time with different size of prefix from a min, to a max.
ex :
XXXXXGGXXXXXGG
with a min=1 and max = 3, it will give :
- 1 : XGG, XGG
- 2 : XXGG, XXGG
- 3 : XXXGG, XXXGG
and then order the result to group the similar prefix.

The application is run like this :
python dna_pattern_finder.py filename_dna_sequence [boolean_rapport pattern size_before_min size_before_max]

Needed parameter is :
- filename_dna_sequence : the file that contains the DNA sequence where we look for the pattern

Optionals parameters are :
- boolean_rapport : 1 or 0. (default is 1).
If 1, save all the output in a file to keep it.
If 0, do not save the output in a file.
- pattern : String with G, A, C or T. (default is "GG")
The pattern we are looking for in the DNA file. Can be anything but only with G, A, C or T.
- size_before_min : the minimum size of the prefix (default is 2)
- size_before_max : the maximum size of the prefix (default is 10)

For simple use, you can just run :

python dna_pattern_finder.py "filename_dna_sequence"

__author__ = "Léo Mullot"
"""


import sys
import os
import re

# Getting parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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

# End of getting parameter >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                        Main code
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

# We get the content of the file that contain DNA sequence
with open(path_file, 'r') as adn_file:
    dna = adn_file.read().replace("\n", "")

# We open a rapport file (or dev/null if user ask for no output
with open(rapport_path, 'w') as rapport_file:
    # For each size of prefix before the pattern
    for size_before in range(size_before_min, size_before_max+1):
        # We reset the res and we update the current place
        res = {}

        # We look for the first occurence
        place = dna.find(pattern, size_before)

        # While there is the pattern in the file (place = -1 when pattern not found)
        while place != -1:
            # We get the prefix before the pattern
            str_before = dna[place-size_before:place+len(pattern)]

            # Then we add it to the res dictionary
            if str_before in res:
                res[str_before] += 1
            else:
                res[str_before] = 1

            # We increment the place of the pattern length to look for a new one.
            place += len(pattern)
            place = dna.find(pattern, place)

        # We output the current res for the current size of prefix
        print("Ordered result for " + str(size_before) + " characters before the pattern.")
        print(sorted(res.items(), key=lambda kv: kv[1], reverse=True))
        print("\n")
