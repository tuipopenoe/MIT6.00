#!python2
# Tui Popenoe
# test_ps4.py - Caesar Cipher Tests

import string
import random
from ps4 import *
import unittest

WORDLIST_FILENAME = 'words.txt'

def test_load_words():
    """ Test the load words method in ps4.py"""
    with open(WORDLIST_FILENAME, 'r') as f:
        wordlist = f.readline().split()
        self.assertEqual(wordlist, load_words())

def test_is_word():
    """Test the is word method in ps4.py"""
    wordlist = load_words()
    test_words = ['All', 'your', 'base', 'are', 'belong', 'to', 'us']
    for word in test_words:
        self.assertEqual((word in wordlist), is_word(wordlist, word))

def test_random_string():
    """Test the random string method in ps4.py"""
    wordlist = load_words()
    random_number = random.randint(10, 20)
    random_string = random_string(wordlist, random_number)
    for word in random_string:
        self.assertTrue(word in wordlist)

def test_random_scrambled():
    """Test the random scrambled method in ps4.py"""
    shift = random.randint(1, 27)
    pass

def test_get_fable_string():
    """Test the get fable string method in ps4.py"""
    raise NotImplementedError()

def test_build_coder():
    """Test the build coder method in ps4.py"""
    shift = random.randomint(1, 27)
    coder = build_coder(shift)
    self.assertTrue(isinstance(coder, dict))
    random_letter = random.choice(string.letters[:25])
    self.assertEqual(coder[random_letter], chr(ord(random_letter) + shift))

def test_build_encoder():
    """Test the build encoder method in ps4.py"""
    test_build_coder()

def test_build_decoder():
    """Test the build decoder method in ps4.py"""
    raise NotImplementedError()

def test_apply_coder():
    """Test the apply coder method in ps4.py"""
    shift = random.randint(1, 27)
    coder = build_coder(shift)
    for i in range(random.randint(15, 30)):
        original_string.append(random.choice(string.letters[:26]))
    shifted_string = ''
    for i in original_string:
        shifted_string.append(coder[i])
    for i in range(len(original_string)):
        test_string.append(chr(ord(original_string[i])))
    self.assertEqual(shifted_string, test_string)

def test_apply_shift():
    """Test the apply shift method in ps4.py"""
    raise NotImplementedError()