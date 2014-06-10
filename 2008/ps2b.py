# Tui Popnenoe
# ps2a.py

def diophantine(tup):
    tmin = tup[0]
    tmed = tup[1]
    tmax = tup[2]

    if tup[0] < tup[1]:
        if tup[1] < tup[2]:
            tmin = tup[0]
            tmed = tup[1]
            tmax = tup[2]
        else:
            tmin = tup[0]
            tmed = tup[2]
            tmax = tup[1]
    else:
        if tup[0] < tup[2]:
            tmin = tup[0]
            tmed = tup[1]
            tmax = tup[2]
        else:
            tmin = tup[0]
            tmed = tup[2]
            tmax = tup[1]


    can = []
    cannot = list(range(1, 200))
    for i in range(1, 200):
        for a in range(tup[0]):
            for b in range(tup[1]):
                for c in range(tup[2]):
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




def main(tup):
    diophantine()

if __name__ == "__main__":
    main()

