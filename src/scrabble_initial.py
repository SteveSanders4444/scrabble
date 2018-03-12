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

length = len(board)
from itertools import permutations
#perms = list(permutations(board))
permlist = []
for j in range(length+1):
    perms = [''.join(i) for i in permutations(board, r=j)]
    #print('permutations of board:', perms)
    #perms = set(perms)  # to dedupe (creates sets {})
    permlist.append(perms)

print(permlist)
print(np.concatenate(permlist))

df = pd.DataFrame(np.concatenate(permlist))
df.columns = ['word']
#df['in_dic'] = bool(df.word in all_words)
#print(df)

'''
for i in range(len(df.word)):
#    print(df.word[i] in all_words)
#    df['in_dic'] = df.word[i] in all_words  # doesn't work
    if df.word[i] in all_words:
        print(df.word[i]+' in all_words')
print(df)
'''
df['in_dic'] = df.word.isin(all_words)
print(df[df['in_dic']==True])

df_realwords = df[df['in_dic']==True]
df_realwords2 = df_realwords.drop_duplicates(subset='word', keep='first')  # drop any duplicate words
df_realwords3 = df_realwords2.drop(columns=['in_dic'])
print(df_realwords3)
print(df_realwords3.shape[0])
#new_index = range(1,df_realwords3.shape[0])
df_realwords4 = df_realwords3.reset_index(drop=True)
print(df_realwords4)



# STEP 4: assign score to each word

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}

word = ''
score_list = []
for i in range(0,df_realwords4.shape[0]):
    word = df_realwords4['word'].loc[i]
    print(word)
    sum = 0
    for letter in word:
        sum += scores.get(letter.lower())
    print(sum)
    score_list.append(sum)

score_list_column = pd.Series(score_list)
df_realwords4.insert(loc=1, column='score', value=score_list_column)
print(df_realwords4)




# STEP 5. find word with maximum score
# STEP 6. return words and scores in descending order of score

result = df_realwords4.sort_values('score', ascending=False)
print(result)

print('Top 20 Scores: ')
for i in range(20):
    print(result.score.iloc[i], ',', result.word.iloc[i])
