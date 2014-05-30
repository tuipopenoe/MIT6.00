import math

def primes(n):
    """ Return a list of primes < n"""
    root = int(math.ceil(math.sqrt(n)))

    if n < 2 :
        return False
    if n % 2 == 0:
        return False

    for i in range(3, root):
        if n % i == 0:
            return False

    return True

def main():
    count = 0
    num = 2

    while count < 1000:
        if primes(num):
            count += 1
            print(count,  "\t" , num)
            num += 1
        else:
            num += 1

if __name__ == "__main__":
    main()