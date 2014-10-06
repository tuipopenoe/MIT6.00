#!python2
# Tui Popenoe
# test_ps2.py - Diophantine Equations

from ps2 import *

def test_diophantine():
    """Test the diophantine method."""
    max_diophantine = 43
    self.assertEqual(max_diophantine, diophantine)

def test_diophantine_constrained():
    """Test the diophantine constrained method."""
    package_size = [(4, 6, 9), (3, 5, 10), (6, 10, 20)]
    max_nums = [50, 100, 150, 200]
    diophantines = [(49, 99, 149, 199), (49, 99, 149, 199), (49, 99, 149, 199)]
    for i in package_size:
        for j in max_nums:
            self.assertEqual(diophantines[i][j], diophantineConstrained(
                package_size[i], max_nums[j]))
