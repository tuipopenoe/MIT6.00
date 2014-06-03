# Tui Popenoe
# ps1a.py
# 2014

import math
import sys

def isPrime(n):
    """Determine if n is prime"""
    if (math.sqrt(n)).is_integer():
        return False
    root = int(math.ceil(math.sqrt(n)))
    if n == 2:
        return True
    if n < 2 :
        return False
    if n % 2 == 0:
        return False
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def main(filename):
    """Return a list of the first 1000 primes"""
    count = 0
    num = 1
    nums = []
    while count < 1000:
        if isPrime(num):
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