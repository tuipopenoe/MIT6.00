#!python2
# Tui Popenoe
# test_ps5_ghost.py

from ps5_ghost import *

def test_is_valid_word(wordlist):
    """
    Unit test for is_valid_word
    """
    failure = False
    # test 1
    word = 'pea'
    if not is_valid_word(word, wordlist):
        print('Failure: test_is_valid_word()')
        print('Expected True, but got false for word: ' + word)
        failure = True
    self.assertEqual(is_valid_word('pea', worldlist), True)

    word = 'pear'
    if is_valid_word(word, wordlist):
        print('Failure: test_is_valid_word()')
        print('Expected False, but got True for word: ' + word)
        failure = True
    self.assertEqual(is_valid_word('pear', wordlist), True)

    word = 'qz'
    if is_valid_word(word, wordlist):
        print('Failure: test_is_valid_word()')
        print('Expected False, but got True for word: ' + word)
        failure = True
    self.assertEqual(is_valid_word('qz', wordlist), False)

    word = 'peafowl'
    if is_valid_word(word, wordlist):
        print('Failure: test_is_valid_word()')
        print('Expected False, but got True for word: ' + word)
        failure = True
    self.assertEqual(is_valid_word('peafowl', wordlist), True)

    if not failure:
        print('SUCCESS: test_is_valid_word()')

word_list = load_words()

print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print('Tests completed')