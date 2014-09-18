#!python2
# Tui Popenoe
# ps2.py

from math import pow

def evaluate_poly(poly, x):
    result = 0
    for i in range(len(poly)):
        result += pow(poly[i] * x, i)
    return result

def compute_deriv(poly):
    if len(poly) <= 1:
        return 0
    else:
        for i in range(len(poly) - 1):
            poly[i] = pow(poly[i + 1], i + 1)
        poly.pop(-1)
    return poly

def compute_root(poly, x_0, epsilon):
    if evaluate_poly(poly, x_0) < epsilon:
        return x_0
    else:
        x_1 = evaluate_poly(poly, x_0) / compute_deriv(poly)
        return compute_root(poly, x_1, epsilon)
