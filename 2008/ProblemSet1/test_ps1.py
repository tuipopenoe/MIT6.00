#!python2
# Tui Popenoe
# test_ps1.py

import unittest
import math
from ps1 import *

def test_is_prime():
    """Test the is prime method."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for i in primes:
        self.assertTrue(isPrime(i))
    for j in non_primes:
        self.assertFalse(isPrime(j))

def test_compute_prime_logs():
    """Test the compute prime logs method."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    self.assertEqual(sum([x for math.log(x) in primes]), computePrimeLogs(30))

def test_compute_first_one_thousand_primes():
    """Test the compute first one thousand primes method."""
    pass