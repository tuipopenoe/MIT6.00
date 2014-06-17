# Tui Popenoe
# ps3a.py


def countSubStringMatch(target, key):
    """ Search string and return count of matching substrings

    Args: 
        target: target string
        key: key string to match against substrings in target
    Rets:
        count of substring matches
    """

    count = 0
    for i in range(0, len(target)-len(key)+1):
        if target[i:i+len(key)] == key:
            count +=1

    return count

def countSubStringMatchRecursive(target, key):
    """ Search string and return count of matching substrings recursively

    Args: 
        target: target string
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