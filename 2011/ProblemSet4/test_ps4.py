#!python2
# Tui Popenoe
# test_ps4.py - Caesar Cipher Tests

import string
import random
import ps4
import unittest

WORDLIST_FILENAME = 'words.txt'

def test_load_words():
    """ Test the load words method in ps4.py"""
    with open(WORDLIST_FILENAME, 'r') as f:
        wordlist = f.readline().split()
        self.assertEqual(wordlist, ps4.load_words())

def test_is_word():
    """Test the is word method in ps4.py"""
    wordlist = ps4.load_words()
    test_words = ['All', 'your', 'base', 'are', 'belong', 'to', 'us']
    for word in test_words:
        self.assertEqual((word in wordlist), ps4.is_word(wordlist, word))

def test_random_string():
    """Test the random string method in ps4.py"""
    wordlist = ps4.load_words()
    random_number = random.randint(10, 20)
    random_string = ps4.random_string(wordlist, random_number)
    for word in random_string:
        self.assertTrue(word in wordlist)

def test_random_scrambled():
    """Test the random scrambled method in ps4.py"""


def test_get_fable_string():
    """Test the get fable string method in ps4.py"""

def test_build_coder():
    """Test the build coder method in ps4.py"""

def test_build_encoder():
    """Test the build encoder method in ps4.py"""

def test_build_decoder():
    """Test the build decoder method in ps4.py"""

def test_apply_coder():
    """Test the apply coder method in ps4.py"""

def test_apply_shift():
    """Test the apply shift method in ps4.py"""
