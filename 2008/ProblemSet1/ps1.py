#!python2
# Tui Popenoe
# ps1.py - Prime Numbers

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
    return primeSum

def computeFirstOneThousandPrimes(filename='primes.txt'):
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
    return nums

def main(filename):
    isPrime(int(raw_input('Enter a number to check if it is prime'))
    computePrimeLogs(int(raw_input('Enter a number to compute the sum of all \
        primes to')))
    computeFirstOneThousandPrimes()

if __name__ == "__main__":
    main(sys.argv[1])