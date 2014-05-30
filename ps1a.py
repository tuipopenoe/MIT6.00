import math
import sys

def primes(n):
    """ Return a list of primes < n"""
    root = int(math.ceil(math.sqrt(n)))
    if n < 2 :
        return False
    if n % 2 == 0:
        return False
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def main(filename):
    count = 0
    num = 2
    nums = []
    while count < 1000:
        if primes(num):
            nums.append(num)
            count += 1
            num += 1
        else:
            num += 1

    f = open(filename, 'w')
    for item in nums:
        f.write("%s\n" %item)

if __name__ == "__main__":
    main(sys.argv[1])