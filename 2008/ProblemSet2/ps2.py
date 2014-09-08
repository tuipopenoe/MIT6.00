#!python2
# Tui Popenoe
# ps2.py - Problem Set 2 - Diophantine Equations

import sys

def diophantine():
    """Return the largest number of mcnuggets less than 50 that cannot be bought
    in exact quantity using a diophantine equation
    Args:
        none
    Rets:
        the largest number under 50 that cannot be bought in exact quantities
    """
    can = []
    cannot = list(range(1,50))
    for i in range(6, 51):
        for a in range(9):
            for b in range(6):
                for c in range(3):
                    if a*6+b*9+c*20 == i:
                        can.append(i)
    for el in can:
        try:
            cannot.remove(el)
        except:
            pass
    print("Cannot make combinations equal to: ")
    print(cannot[-6:])
    print("Largest integer that cannot form a combo: ")
    print(cannot[-1])
    return(cannot[-1:])

def diophantine(t, m):
    """Return the largest number less than 200 that cannot be bought in exact
    quantity. 

    Args:
        t: tuple of package sizes
        m: largest size
    Rets:
        list of sizes that cannot be created exactly
    """
    lst = list(t)
    lst.sort()
    tmin = lst[0]
    tmed = lst[1]
    tmax = lst[2]
    print(tmin, tmed, tmax)
    inflection = 2*tmin + 2*tmed + tmax;
    can = []
    cannot = list(range(1, (m)))
    for i in range(1, inflection):
        for a in range(tmed):
            for b in range(tmin):
                for c in range(int(tmax/tmin)):
                    if a*tmin+b*tmed+c*tmax == i:
                        can.append(i)
    for el in can:
        try:
            cannot.remove(el)
        except:
            pass
    print("Cannot make combinations equal to: ")
    print(cannot[-6:])
    print("Largest integer that cannot form a combo: ")
    print(cannot[-1])
    return(cannot[-1:])

def main():
    diophantine()
    diophantine(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
