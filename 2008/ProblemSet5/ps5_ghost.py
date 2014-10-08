#!python2
# Tui Popenoe
# ps5_ghost.py

import random

import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def is_valid_word(word, wordlist):
    if len(word) < 3:
        if not any(word in x for x in wordlist):
            print("Impossible String")
            return False
    if len(word) > 3:
        if word in wordlist:
            print("Word longer than 4 and in wordlist: ")
            return False
        if not any(word in x for x in wordlist):
            print("Word longer than 4 and no words remaining")
            return False
    return True

def ghost(wordlist):
    current_word = ''
    player = 2
    while True:
        if player == 1:
            player = 2
        else:
            player = 1
        print('Player %s' %player)
        print('Current Word: ' + current_word)
        letter = raw_input('Enter a letter to extend the word: ')
        while len(letter) != 1:
            letter = raw_input('Enter a valid letter: ')
        current_word += letter
        if is_valid_word(current_word, wordlist):
            pass
        else:
            print('Invalid entry, player %s loses' % str(player))
            break

if __name__ == '__main__':
    word_list = load_words()
    ghost(word_list)

