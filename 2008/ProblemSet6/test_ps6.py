#!python2
# Tui Popenoe
# test_ps6.py

from ps6 import *

def test_load_words():
    """Test the load words method."""
    with open('words.txt', 'r') as wordlist:
        wordlist = wordlist.readlines().strip().lower()
        self.assertEqual(wordlist, load_words)

def test_get_frequency_dict():
    """Test the get frequency dict method."""
    test_words = 'abbcccddddeeeee'
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    self.assertEqual(test_dict, test_get_frequency_dict(test_words))

def test_get_word_score():
    """Test the get word score method."""
    test_vals = [('')]
    raise NotImplementedError()

def test_display_hand():
    """Test the display hand method."""
    raise NotImplementedError()

def test_update_hand():
    """Test the update hand method."""
    word = 'a'
    test_hand = {'a': 1, 'b': 1}
    new_hand = {'b': 1}
    self.assertEqual(update_hand(test_hand, word), new_hand)

def test_is_valid_word():
    """Test the is valid word method."""
    raise NotImplementedError()

def test_play_hand():
    """Test the play hand method."""
    raise NotImplementedError()

def test_play_game():
    """Test the play game method."""
    raise NotImplementedError()