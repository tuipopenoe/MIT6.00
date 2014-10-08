#!python2
# Tui Popenoe
# ps3.py

#import string

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def countSubStringMatch(target, key):
    """ Search string and return count of matching substrings

    Args: 
        target: target string
        key: key string to match against substrings in target
    Rets:
        count of substring matches
    """
    count = 0
    for i in range(0, len(target) - len(key) + 1):
        if target[i:i + len(key)] == key:
            count += 1
    return count

def countSubStringMatchRecursive(target, key):
    """ Search string and return count of matching substrings recursively

    Args: 
        target: target string to search
        key: key string to match against substrings in target
    Rets:
        count of substring matches
    """
    if len(target) < len(key) or len(target) < 0:
        return 0
    if target[0:len(key)] == key:
        return 1 + countSubStringMatchRecursive(target[1:], key)
    else:
        return 0 + countSubStringMatchRecursive(target[1:], key)

def subStringMatchExact(target, key):
    """Search target string and return locations of matching strings

    Args:
        target: target string to search
        key: key string to match against substrings in the target
    Rets:
        tuple of indices where a match begins
    """
    match = []
    for i in range(0, len(target) - len(key) + 1):
        if target[i:i+len(key)] == key:
            match.append(i)
    return tuple(match)

def constrainedMatchPair(firstMatch, secondMatch, length):
    """Returns member of firstMatch where there is an element in secondMatch
    such that n + m + 1 = k

    Args:
        firstMatch: tuple of starting points for first substring
        secondMatch: tuple of starting points for second substring
        length: length of the first substring
    Rets:
        tuple of matches for which n + m + 1 = k
    """
    matches = []
    for i in firstMatch:
        for j in secondMatch:
            if i + length + 1 == j:
                matches.append(i)
    return tuple(matches)

def subStringMatchOneSub(target, key):
    """Search for all locations of key in target with one substitution

    Args:
        target: target string to search
        key: key string to match against substrings in the target
    Rets:
        tuple of indices of matches with one substitution
    """
    allAnswers = ()
    for miss in range(0, len(key)):
        key1 = key[:miss]
        key2 = key[mis+1:]
        #'breaking key', key, 'into', key1, key2
        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)
        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        #'match1', match1
        #'match2', match2
        #'possible matches for', key1, key2,'start at', filtered
    return allAnswers

def subStringMatchExactlyOneSub(target, key):
    """Search for all locations of key in target with exactly one substitution
    Args:
        target: target string to search
        key: key string to match against substrings in the target
    Rets:
        tuple of all starting points of matches of the key to the target 
        where exactly one element of the key is incorrectly matched to the 
        target
    """
    exact = subStringMatchExact(target, key)
    oneSub = subStringMatchOneSub(target, key)
    exactlyOneSub = [x for x in oneSub if x not in oneSub]
    return tuple(exactlyOneSub)
