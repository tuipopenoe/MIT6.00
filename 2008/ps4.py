# Tui Popenoe
# MIT 6.00 ps4

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
    # possibleExpenses = 
    #     range(nestEggVariable(salary, save, preRetireGrowthRates)[-1])

    
def testNestEggFixed():

def testNestEggVariable():

def testPostRetirement():

def testFindMaxExpenses():
