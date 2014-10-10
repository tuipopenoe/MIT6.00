#!python2
# Tui Popenoe
# test_ps8.py - Dynamic Programming

from ps8.py import *

def test_load_subjects():
    """Test the load subjects method."""
    d = {'class1': (1, 1),
         'class2': (2, 2),
         'class3': (3, 3),
         'class4': (4, 4),
         'class5': (5, 5)
        }
    with open('test_subjects.txt', 'a+') as f:
        for key, value in d.iteritems():
            f.write(key%s%s%s%s, % (',', value[0], ',', value[1]))
    x = loadSubjects('test_subjects.txt')
    assert(x, d)

def test_print_subjects():
    """Test the print subjects method"""
    raise NotImplementedError()

def test_cmp_value():
    """Test the cmp value method."""
    values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    values2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for val i range(10):
        assert(cmpValue(values2[i], values1[i]))

def test_cmp_work():
    """Test the cmp work method."""
    values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    values2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for val in range(10):
        assert(cmpWork(values2[i], values1[i]))

def test_greedy_advisor():
    """Test the greedy advisor method."""
    