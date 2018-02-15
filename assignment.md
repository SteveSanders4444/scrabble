# Assignment: Scrabble Cheater

This week you will be building a little tool to help you cheat at Scrabble. This program is adapted from an assignment that you can find online (https://openhatch.org/wiki/Scrabble_challenge).

The core goals of this project are to help you practice problem solving with Python from scratch. You will use the command line, write functions (and possibly classes), and practice reading in files as well as working with dictionaries and for loops. By the end of the assignment you should feel confident doing the above. Although answers may exist online, we encourage you to try and do as much as you can without any guidance. The purpose of this course is to teach you how to figure out how to solve problems using a programming language, not to copy and paste answers from the Internet. We believe that you have the skills to do this.

## Assignment Description

Write a command line based Python script that takes a Scrabble rack as an argument and prints all valid words that can be constructed from that rack along with their associated scores. An example of its invocation is below.

```sh
$ python scrabblecheater.py zadddhy
19,hazy
13,adz
11,daddy
11,za
9,yah
9,addy
9,hay
9,dyad
7,had
7,dah
7,yad
7,day
5,dad
5,ya
5,ah
5,add
5,ay
5,ha
3,ad
3,da
```

## Resources
You will find a file in this folder labeled all_words.zip. Unzip that file and use those words as your official valid words. Below you will find a dictionary containing all letter values that you may use.
*Italic generated but not needed.*

```python
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}
```


## Tips
The order of operations and what you should be building first may seem difficult, but it is actually quite straightforward. Here are the steps that we recommend you perform, in order.

1. Open the files and construct the word list. (You may unzip the zip file manually.)
2. Get the rack from the command line.
3. Find all the words that are a subset of the letters in the rack you were given.
4. Score each of the words.
