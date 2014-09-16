#!python2
# Tui Popenoe
# ps1.py - Paying Credit Card Debt

def pay_minimum():
    balance = float(raw_input('Enter the outstanding balance on the card: '))
    apr = float(raw_input('Enter the annual percentage rate of interest: '))
    minimum_payment_rate = float(raw_input('Enter the minimum payment rate: '))
    interest = apr / 12.0
    interest_paid = 0
    principal_paid = 0
    total_paid = 0
    for i in range(12):
        interest_paid = interest * balance
        principal_paid = (minimum_payment_rate * balance) - interest_paid
        balance -= principal_paid
        total += principal_paid + interest_paid
        print('Month ' + i + 1)
        print('Minimum Monthly Payment: ' + str(minimum_payment_rate * balance))
        print('Principal paid: ' + str(principal_paid))
        print('Remaining balance: ' + str(balance))
        print('Total paid: ' + str(total))

def payoff_year_linear():
    balance = float(raw_input('Enter the outstanding balance on the card: '))
    apr = float(raw_input('Enter the annual percentage rate of interest: '))
    monthly_interest = apr / 12.0
    base = balance
    for i in range(10, balance, 10):
        for j in range(12):
            balance = balance * (1 + monthly_interest) - i
            if balance < 0:
                print('Monthly payment to pay off debt in one year: ' + str(i))
                print('Number of months needed: ' + str(j))
                print(str(balance))
                break
        balance = base

def payoff_year_logarithmic():
    balance = float(raw_input('Enter the outstanding balance on the card: '))
    apr = float(raw_input('Enter the annual percentage rate of interest: '))
    monthly_interest = apr/12.0
    low = 0
    high = balance
    endBalance = balance
    base = balance
    while abs(endBalance) > 0:
        guess = (low + high) / 2 
        for i in range(12):
            balance = balance * (1 + monthly_interest) - guess
        if endBalance > 0:
            low = guess
        else:
            high = guess
        balance = base

    return guess