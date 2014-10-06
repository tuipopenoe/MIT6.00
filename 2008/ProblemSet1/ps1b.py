# Tui Popenoe
# ps1b.py
# 2014

import math
import sys

def computePrimeLogs(n):
    """Computes the sum of the logarithms of all primes from 2 to n"""

    primeSum = 0
    for i in range(n):
        if(isPrime(i)):
            primeSum += math.log(i)

    ratio = primeSum / n

    print("Sum of Logs of Primes: ", primeSum)
    print("N: ", n)
    print("Ratio: ", ratio)



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

def main(n):
    computePrimeLogs(int(n))

if __name__ == "__main__":
    main(sys.argv[1])