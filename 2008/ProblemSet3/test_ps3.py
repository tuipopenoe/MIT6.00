#!python
# Tui Popenoe
# test_ps3.py

from ps3 import *
import unittest

def test_count_sub_string_match():
    """Test the count sub string match method."""
    test_strings = [('abababbbabba', 'ab', 4), ('cdabcabcdbacc', 'bc', 2),
                    ('abcdeffecdabeafde', 'cd', 2), ('aaaaaa', 'a', 6)]
    for i in test_strings:
        self.assertEqual(countSubStringMatch(i[0], i[1]), i[2])

def test_count_sub_string_match_recursive():
    """Test the count sub string match recursive method."""
    test_strings = [('abababbbabba', 'ab', 4), ('cdabcabcdbacc', 'bc', 2),
                    ('abcdeffecdabeafde', 'cd', 2), ('aaaaaa', 'a', 6)]
    for i in test_strings:
        self.assertEqual(countSubStringMatch(i[0], i[1]), i[2])

def test_sub_string_match_exact():
    """Test the sub string match exact method."""
    test_strings = [('abababab', 'ab', (0, 2, 4)), ('aaaaaacdddd', 'ac', (,5)),
        ('efdefdadacabada', 'da', (4, 6, 12)), ('abcd', 'bc', (,1)]
    for i in test_strings:
        self.assertEqual(countSubStringMatch(i[0], i[1]), i[2])

def test_constrained_match_pair():
    """Test the constrained match pair method."""
    raise NotImplementedError()

def test_sub_string_match_one_sub():
    """Test the sub string match one sub method."""
    test_strings = [('bedbedbud', 'bad', (0, 3, 6)), ('toptiptaptup', 'tep',
        (0, 3, 6, 9)), ('fixfaxfoxflex', 'fyx', (0, 3, 6))]
    for i in test_strings:
        self.assertEqual(subStringMatchOneSub(i[0], i[1]), i[2])