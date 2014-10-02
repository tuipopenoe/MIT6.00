#!python2
# Tui Popenoe
# ps4.py - Caesar ciphers

characters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z']

import string
import random


def load_words(filename='words.txt'):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(filename, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()


def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist


def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])


def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] ==
              ' ']
    return apply_shifts(s, shifts)[:-1]


def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.
    """
    cipher = {}
    if shift > 27:
        shift = 27
    if shift < 1:
        shift = 1
    for i in range(len(characters)):
        cipher[characters[i]] = characters[(i + shift) % 27]
        if characters[i] != ' ':
            cipher[characters[i].upper()] = characters[(i + shift) % 27]
            .upper()
    print(cipher)
    return cipher


def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. The cipher is
    defined by the shift value. Ignores non-letter characters like punctuation
    and numbers.
    """
    cipher = {}
    if shift > 27:
        shift = 27
    if shift < 1:
        shift = 1
    for i in range(len(characters)):
        cipher[characters[i]] = characters[(i + shift) % 27]
        if characters[i] != ' ':
            cipher[characters[i].upper()] = characters[(i + shift) % 27]
            .upper()
    print(cipher)
    return cipher

def build_decoder(shift):
    """
    Returns a dict that can be used to decode encrypted text.

    Args:
        shift - int between 0 and 27
    Rets:
        dict
    """
    coder = build_coder(shift)
    decoder = dict(zip(coder.values(), coder.keys()))
    return decoder


def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    Args:
        text - a string to be coded
        coder - dict with mappings of characters to shifted characters
    Rets:
        text - string after being mapped to original text
    """
    coded_text = ''
    for i in text:
        coded_text += coder[i]
    return coded_text


def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar cipher shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet, so
    spaces are replaced by lowercase letters.

    Args:
        text - string to apply the shift to.
        shift - amount to shift the text
    Rets:
        text after being shifted by specified amount
    """
    shifted_text = ''
    coder = build_coder(shift)
    for i in text:
        if i in coder:
            shifted_text += coder[i]
        else:
            shifted_text += i
    return shifted_text


def main():
    build_coder(3)

if __name__ == '__main__':
    main()
