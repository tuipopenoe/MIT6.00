# Tui Popenoe
# ps3b.py

import string

def subStringMatchExact(target, key):
    match = []
    for i in range(0, len(target) - len(key) + 1):
        if target[i:i+len(key)] == key:
            match.append(i)

    return tuple(match)