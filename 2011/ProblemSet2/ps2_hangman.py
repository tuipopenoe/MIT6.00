#!python2
# Tui Popenoe
# ps2_hangman.py

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Args:
        None
    Rets:
        list of words
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def play_game():
    wordlist = load_words()
    available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                         'w', 'x', 'y', 'z']
    word = choose_word(wordlist)
    guesses = len(word) + 2
    blanks = ['_' for i in range(len(word))]
    while guesses > 0:
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + ''.join(available_letters))
        letter = raw_input('Please guess a letter: ').lower()
        while len(letter) != 1:
            letter = raw_input('Please guess a letter: ').lower()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    blanks[i] = letter
            print('Good guess: ' + ''.join(blanks))
            available_letters.remove(letter)
        else:
            print('Oops! That letter is not in my word: ' + ''.join(blanks))
        guesses -= 1
        if blanks == word and guesses > 0:
            print('Congratulations, you won!')
            break
        elif guesses < 1:
            print('You Lose! Word was: ' + word)


def main():
    play_game()

if __name__ == '__main__':
    main()
