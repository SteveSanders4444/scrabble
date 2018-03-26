# scrabble program
# Object Oriented version

# Steve Sanders
# 3/24/18

# run from command line.  Example: $python3 scrabble_oo.py testword

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
from itertools import permutations
# from __future__ import print_function  # for coding in Python2


class Scrabble:

    '''
    Scrabble class takes a user-inputted series of letters and and external valid-word list.
    It finds permutations of the letters that match valid words and scores each one.
    '''

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10}

    def __init__(self, board = None, all_words = None):
        self.board = board
        self.all_words = all_words
        self.length = len(self.board)
        self.df_realwords4 = ''


    def match_real_words(self):
        permlist = []
        for j in range(self.length+1):
            perms = [''.join(i) for i in permutations(self.board, r=j)]
            #print('permutations of board:', perms)
            #perms = set(perms)  # to dedupe (creates sets {})
            permlist.append(perms)

        df = pd.DataFrame(np.concatenate(permlist))
        df.columns = ['word']

        df['in_dic'] = df.word.isin(self.all_words)

        df_realwords = df[df['in_dic']==True]
        df_realwords2 = df_realwords.drop_duplicates(subset='word', keep='first')  # drop any duplicate words
        df_realwords3 = df_realwords2.drop(columns=['in_dic'])
        self.df_realwords4 = df_realwords3.reset_index(drop=True)


    def score_words(self):
        word = ''
        score_list = []
        for i in range(0,self.df_realwords4.shape[0]):
            word = self.df_realwords4['word'].loc[i]
            sum = 0
            for letter in word:
                sum += Scrabble.scores.get(letter.lower())  # need to specify class attribute 'scores'
            score_list.append(sum)

        score_list_column = pd.Series(score_list)
        self.df_realwords4.insert(loc=1, column='score', value=score_list_column)


    def sort_words(self):
        result = self.df_realwords4.sort_values('score', ascending=False)
        result_length = len(result)
        print(result_length)
        if result_length < 20:
            loop_len = result_length
        else:
            loop_len = 20

        print('Top Scores: ')
        for i in range(loop_len):
            print(result.score.iloc[i], ',', result.word.iloc[i])




try:
    # STEP 1 : read text file containing valid words
    with open('all_words.txt', 'rt') as all_words:
        all_words = list(all_words)
        all_words = [i.strip() for i in all_words]  # strip '/n'


    # STEP 2: input user board containing letters
    print(sys.argv)
    if len(sys.argv) > 1:
        board = sys.argv[1]
    else:
        board = input("Enter your board letters: ")
    board = board.upper()


    scrabble_play = Scrabble(board, all_words)  # instantiate Scrabble object
    
    # run the following methods in order:
    scrabble_play.match_real_words()
    scrabble_play.score_words()
    scrabble_play.sort_words()

except Exception as e:
    print("There was an error:", e)
    # Uncomment this line for full error messages
    #traceback.print_exc(file=sys.stdout)
