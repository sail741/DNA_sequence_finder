# DNA_sequence_finder

## Information

### Credit 
* By Léo Mullot
* For the LiMMS
* In 2018

### Description
This application look into a file that contains DNA sequence (GCGCGTACG...) to find a pattern, and compare the prefix of the pattern.
Actually, the application is run multiple time with different size of prefix from a min, to a max.
ex :
XXXXXGGXXXXXGG
with a min=1 and max = 3, it will give :
- 1 : XGG, XGG
- 2 : XXGG, XXGG
- 3 : XXXGG, XXXGG
and then order the result to group the similar prefix.

## Requirement

* Python3

## Running application

### Simple usage

To run the application with default parameter, just run : 
```
python dna_pattern_finder.py "filename_dna_sequence"
```

### Specific usage

To run the application with specific parameter, you can give few arguments to the app :
```
python dna_pattern_finder.py filename_dna_sequence [boolean_rapport pattern size_before_min size_before_max]
```

Needed parameter is :
* filename_dna_sequence : the file that contains the DNA sequence where we look for the pattern

Optionals parameters are :
* **boolean_rapport** : 1 or 0. (default is 1).
  * If 1, save all the output in a file to keep it.
  * If 0, do not save the output in a file.
* **pattern** : String with G, A, C or T. (default is "GG")
  * The pattern we are looking for in the DNA file. Can be anything but only with G, A, C or T.
* **size_before_min** : the minimum size of the prefix (default is 2)
* **size_before_max** : the maximum size of the prefix (default is 10)

Example for specifig usage :
```
python dna_pattern_finder.py dna_sequence.txt 1 CGC 5 8
```
Wich mean "look in the file dna_sequence.txt, output the result in a rapport file, and search the pattern 'CGC' and the prefix in the DNA sequence. The prefix will be printed from 5 to 8 char.
