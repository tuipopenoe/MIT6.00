# Tui Popenoe
# ps3c.py

import string
import ps3b

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def constrainedMatchPair(firstMatch, secondMatch, length):
    for i in range
        if == 

def subStringMatchOneSub(target, key):
    """Search for all locations of key in target with one substitution"""
    allAnswers = ()
    for miss in range(0, len(key)):
        key1 = key[:miss]
        key2 = key[mis+1:]
        print 'breaking key', key, 'into', key1, key2

        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)

        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered

        print 'match1', match1
        print 'match2', match2
        print 'possible matches for', key1, key2,'start at', filtered

    return allAnswers