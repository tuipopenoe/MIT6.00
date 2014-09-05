# Tui Popenoe
# MIT 6.00 ps4

from bisect import bisect_left

def nestEggFixed(salary, save, growthRate, years):
    F = list()
    F.append(salary * save * 0.01)
    for i in range(1, years+1):
        F.append(F[i-1] *(1+0.01*growthRate) +salary * save *0.01)
    return F

def nestEggVariable(salary, save, growthRates):
    F = list()
    F.append(salary * save * 0.01)
    for i in range(len(growthRates)):
        F.append(F[i-1] * (1+0.01*growthRates[i]) + salary * save * 0.01)
    return F

def postRetirement(savings, growthRates, expenses):
    F = list()
    F.append(savings)
    for i in range(len(growthRates)):
        F.append(F[i-1] * (1+0.01*growthRates[i]) -expenses)
    return F

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
    epsilon):
    savingsAtStart = nestEggVariable(salary, save, preRetireGrowthRates)
    possibleExpenses = [x for x in range(0, int(max(savingsAtStart)))]
    #for i in possibleExpenses:


    #     range(nestEggVariable(salary, save, preRetireGrowthRates)[-1])

def binary_search(a, x, lo=0, hi=None):
    if hi is not None:
        hi = hi
    else:
        hi = len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)
