# Tui Popnenoe
# ps2a.py

def diophantine():
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




def main():
    diophantine()

if __name__ == "__main__":
    main()

