#!python2
# Tui Popenoe
# test_ps4.py

from ps4 import *

def test_nest_egg_fixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    test_vals = [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]
    self.assertEqual(savingsRecord, test_vals)

def test_nest_egg_variable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    test_vals = [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]
    self.assertEqual(savingsRecord, test_vals)

def test_post_retirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    test_vals = [80000.000000000015, 54000.000000000015, 24000.000000000015,
    self.assertEqual(savingsRecord, test_vals)

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    test_val = 1229.95548986
    self.assertEqual(expenses, test_val)

print("----------------------------------------------------------------------")
print("Testing nestEggFixed...")
testNestEggFixed()
print("----------------------------------------------------------------------")
print("Testing nestEggVariable...")
testNestEggVariable()
print("----------------------------------------------------------------------")
print("Testing postRetirement...")
testPostRetirement()
print("----------------------------------------------------------------------")
print("Testing findMaxExpenses...")
testFindMaxExpenses()
print "----------------------------------------------------------------------"
print "All done!"