# Tui Popnenoe
# ps2a.py

import sys

def diophantine(t, m):
    print(t)
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




def main(t, m):
    diophantine(t, m)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

