#!python2
# Tui Popenoe
# MIT 6.00 ps4

from bisect import bisect_left

def nestEggFixed(salary, save, growthRate, years):
    """Determine the size of retirement savings after a given number of years
    Args:
        salary: fixed salary throughout the time period
        save: percentage of salary that is saved in retirement fund
        growthRate: rate of growth of savings/investments
        years: number of years until retirement
    Rets:
        a list of the values of the retirement fund after every year
    """
    F = []
    F.append(salary * save * 0.01)
    for i in range(1, years):
        F.append(F[i-1] * (1 + 0.01 * growthRate) + salary * save * 0.01)
    return F

def nestEggVariable(salary, save, growthRates):
    """Determine the size of retirement savings given a variable growth rate 
    throughout the savings period
    Args:
        salary: initial salary
        save: percentage of salary saved
        growthRates: list of growthRates for each year
    Rets:
        a list of the values of the retirement fund after every year
    """
    F = []
    F.append(salary * save * 0.01)
    for i in range(1, len(growthRates)):
        F.append(F[i-1] * (1+0.01*growthRates[i]) + salary * save * 0.01)
    return F

def postRetirement(savings, growthRates, expenses):
    """Determine the size of retirement savings given a variable growthrate 
    upon a fixed principal, subtracting yearly expenses
    Args:
        savings: principal of the account
        growthRates: list of growth rates for the accounts
        expenses: amount spent every year
    Rets:
        list of the value of the retirement fund after every year
    """
    F = []
    F.append(savings * (1 + 0.01 * growthRates[0]) - expenses)
    for i in range(1, len(growthRates)):
        F.append(F[i-1] * (1 + 0.01 * growthRates[i]) - expenses)
    return F

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
    epsilon):
    """Determine the maximum amount of expenses that can be spent every year 
    such that at the end of retirement, that total amount of the fund is less
    than epsilon.
    Args:
        salary: salary during saving period
        save: percentage of salary to save
        preRetireGrowthRates: growth rates during the saving period
        postRetireGrowthRates: growth rates after the principal is accumulated
        epsilon: the amount the fund must be less than after retirement
    Rets:
        list of the maximum expenses for each year of retirement
    """
    fundsize = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    yearsOfRetirement = len(postRetireGrowthRates)

    for growthRate in postRetireGrowthRates:
        expenses = calculateExpenses(fundsize, epsilon, yearsOfRetirement)
        fundsize = (fundsize * (1 + 0.01 * growthRate))
        print('Size of Retirement Savings: ' + str(fundsize))
        print('Maximum Expenses for the year: ' + str(expenses))
    return fundsize


def calculateExpenses(fundsize, epsilon, yearsOfRetirement):
    low = 0
    high = fundsize
    guess = (low + high) / 2
    while abs(guess * yearsOfRetirement - fundsize) > epsilon:
        if guess * yearsOfRetirement > fundsize:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    return guess
