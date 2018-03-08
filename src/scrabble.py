# scrabble program

# Steve Sanders
# 3/7/18

# run from command line

'''
Steps:
1. read text file containing valid words
2. input user board containing letters
3. for every combination of inputted letters and every subset, return list of ALL matching words
4. assign score to each words
5. find word with maximum score
6. return words and scores in descending order of score



'''


## IMPORTS ##
import sys
import numpy as np
import matplotlib as plt
import pandas as pd
# from __future__ import print_function  # for coding in Python2


# STEP 1 : read text file containing valid words
with open('all_words.txt', 'rt') as all_words:
    all_words = list(all_words)
    all_words = [i.strip() for i in all_words]  # strip '/n'
    #print(type(all_words))
    #print(len(all_words))
    #print(all_words[0:5])
    #print([word for word in all_words if word[0:3]=='WOR'])
    #for line in all_words:
    #    print(line)



# STEP 2: input user board containing letters
print(sys.argv)

if len(sys.argv) > 1:
    board = sys.argv[1]
else:
    board = input("Enter your board letters: ")

board = board.upper()


# quick check....
if board in all_words:
    print(board + ' in all_words')
else:
    print(board + ' not in all_words')



# STEP 3: for every combination of inputted letters and every subset, return list of ALL matching all_words
# - check original word
# - check all combinations of letters in the original word
# - for all letters in original word, remove one letter and check all letter combinations
# -    remove 2 letters and check all combinations
# -    continue until all letters removed
# - dedupe matching words
