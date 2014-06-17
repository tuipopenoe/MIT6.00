# Tui Popenoe
# ps3a.py


def countSubStringMatch(target, key):
    count = 0
    for i in range(0, len(target)-len(key)+1):
        if target[i:i+len(key)] == key:
            count +=1

    return count

def countSubStringMatchRecursive(target, key):
    if len(target) < len(key) or len(target) < 0:
        return 0
    if target[0:len(key)] == key:
        return 1 + countSubStringMatchRecursive(target[1:], key)
    else:
        return 0 + countSubStringMatchRecursive(target[1:], key)