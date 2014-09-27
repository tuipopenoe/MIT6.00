#!python2
# Tui Popenoe
# ps2.py

from math import pow


def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Args:
        poly: tuple of numbers, length > 0
        x: number
    Rets:
        float
    """
    result = 0
    for i in range(len(poly)):
        result += poly[i] * pow(x, i)
    return result


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Args:
        poly: tuple of numbers, length > 0
    Rets:
        tuple of numbers
    """
    result = []
    if len(poly) <= 1:
        return 0
    else:
        for i in range(len(poly) - 1):
            result.append(poly[i+1] * (i + 1))
    return tuple(result)


def compute_root(poly, x_0, epsilon, count=0):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Args:
        poly: tuple of numbers, length > 1.
            Represents a polynomial function containing at least one real root.
            The derivative of this polynomial function at x_0 is not 0.
        x_0: float
        epsilon: float > 0
    Rets:
        tuple (float, int)
    """
    if abs(evaluate_poly(poly, x_0)) < abs(epsilon):
        print(evaluate_poly(poly, x_0))
        return (x_0, count)
    else:
        x_1 = x_0 - (evaluate_poly(poly, x_0) /
                     evaluate_poly(compute_deriv(poly), x_0))
        return compute_root(poly, x_1, epsilon, count+1)


def test_evaluate_poly():
    """
    Test the evaluate_poly() method.

    Args:
        None
    Rets:
        None
    """
    poly = (0.0, 0.0, 5.0, 9.3, 7.0)
    x = -13
    assert evaluate_poly(poly, x) == 180339.9


def test_compute_deriv():
    """
    Tests the compute_deriv() method

    Args:
        None
    Rets:
        None
    """
    poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
    assert compute_deriv(poly) == (0.0, 35.0, 9.0, 4.0)


def test_compute_root():
    """
    Tests the compute_root() method

    Args:
        None
    Rets:
        None
    """
    poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
    x_0 = 0.1
    epsilon = 0.0001
    print(compute_root(poly, x_0, epsilon))
    assert compute_root(poly, x_0, epsilon) == (0.80679075379635201, 8)


def main():
    test_evaluate_poly()
    test_compute_deriv()
    test_compute_root()

if __name__ == '__main__':
    main()
