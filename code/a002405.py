from math import gcd, factorial

# py-polynomial==0.6.0
# Py-Polynomial by Alexander Ignatov
# https://github.com/allexks/py-polynomial
from polynomial import Polynomial as P


# GENERAL MATH
def choose(p, j):
    """
    >>> choose(1, 1)
    1
    >>> choose(1, 2)
    2
    >>> choose(1, 3)
    3
    """
    return factorial(j) // (factorial(p) * factorial(j - p))


def triangle_index(n):
    """
    >>> triangle_index(0)
    (0, 0)
    >>> triangle_index(1)
    (0, 1)
    >>> triangle_index(2)
    (1, 1)
    >>> triangle_index(6)
    (0, 3)
    >>> triangle_index(7)
    (1, 3)
    """
    m = n
    i = 0
    while i < m:
        m = m - i - 1
        i = i + 1
    return (m, i)


# PICKARD - HELPERS
def L(n):
    """
    This is A003418(n+1).
    >>> L(5)
    60
    >>> L(4)
    60
    >>> L(6)
    420
    """
    if n == 0:
        return 1
    p = L(n - 1)
    return (n + 1) * p // gcd(n + 1, p)


def L_factorial(n):
    """
    L(n)n! is the denominator that is multiplied out
    in several places.
    For example, Alef(n) = L(n)n!beta(n)
    and delta(p, J) = L(n)n!alpha(p, J)
    >>> L_factorial(6)
    302400
    """
    return L(n) * factorial(n)


def A(n, m):
    """
    We use this to change between fractions
    that have been multiplied out by different denominators.
    This means that we can do all the calculations with integers.
    >>> A(1, 3)
    36
    >>> A(2, 3)
    6
    """
    return L_factorial(m) // L_factorial(n)


def gamma(p, j):
    """
    Pickard doesn't define this symbol anywhere.
    It is used in (13a) and (14a).
    Its meaning is made clear in (12).
    >>> gamma(1, 1)
    -1
    >>> gamma(1, 3)
    -3
    >>> gamma(2, 4)
    6
    """
    return (-1) ** p * choose(p, j)


# PICKARD - TABULATED SYMBOLS
def Alef(n):
    """
    >>> Alef(1)
    1
    >>> Alef(2)
    5
    >>> Alef(3)
    27
    >>> Alef(6)
    95435
    >>> Alef(9)
    262426878
    """
    a = P(1)
    for i in range(0, n):
        a = a * P(1, i)

    # This is the integral between 0 and 1
    # Preferable to calculate term-by-term using integers
    x = 0
    for b, d in a.terms:
        x = x + b * (L(n) // (d + 1)) 
    return x


def Alef_star(n):
    """
    >>> Alef_star(0)
    1
    >>> Alef_star(6)
    -4315
    >>> Alef_star(3)
    -3
    >>> Alef_star(9)
    -7217406
    """
    a = P(1)
    for i in range(0, n):
        a = a * P(1, i)
    
    # This is the integral between 0 and 1
    # Preferable to calculate term-by-term using integers
    x = 0
    for b, d in a.terms:
        x = x + b * (-1)**d * (L(n) // (d + 1)) 
    return x


def delta(p, J):
    """
    >>> delta(0, 0)
    1
    >>> delta(0, 1)
    3
    >>> delta(0, 2)
    23
    >>> delta(1, 2)
    -16
    >>> delta(2, 2)
    5
    >>> delta(3, 3)
    -27
    >>> delta(0, 3)
    165
    >>> delta(1, 3)
    -177
    """
    return sum(gamma(p, j) * A(j, J) * Alef(j) for j in range(p, J + 1))


def delta_star(p, J):
    """
    >>> delta_star(0, 0)
    1
    >>> delta_star(0, 1)
    1
    >>> delta_star(0, 2)
    5
    >>> delta_star(2, 2)
    -1
    >>> delta_star(3, 3)
    3
    """
    return sum(gamma(p, j) * A(j, J) * Alef_star(j) for j in range(p, J + 1))


# OEIS SEQUENCES
def A002397(n):
    """
    >>> A002397(1)
    2
    >>> A002397(2)
    12
    >>> A002397(3)
    72
    >>> A002397(6)
    302400
    >>> A002397(9)
    914457600
    """
    return L_factorial(n)


def A002398(n):
    """
    >>> A002398(3)
    165
    """
    return delta(0, n)


def A002399(n):
    """
    >>> A002399(3)
    -177
    """
    return -delta(1, n)

A002399.start = 1


def A002400(n):
    """
    >>> A002400(3)
    111
    """
    return delta(2, n)

A002400.start = 2


def A002401(n):
    """
    >>> A002401(1)
    1
    >>> A002401(2)
    5
    >>> A002401(3)
    27
    >>> A002401(4)
    502
    >>> A002401(6)
    95435
    >>> A002401(9)
    262426878
    """
    return Alef(n)


def A002402(n):
    """
    >>> A002402(3)
    57
    >>> A002402(6)
    325560
    """
    return delta_star(1, n)


def A002403(n):
    """
    >>> A002403(3)
    -15
    >>> A002403(7)
    -4262895
    """
    return delta_star(2, n)


def A002404(n):
    """
    >>> A002404(0)
    3
    >>> A002404(1)
    -16
    >>> A002404(3)
    -2548
    >>> A002404(4)
    14385
    """
    return delta(n, n + 1)


def A002405(n):
    """
    >>> A002405(1)
    -1
    >>> A002405(2)
    -1
    >>> A002405(3)
    -3
    >>> A002405(6)
    -4315
    >>> A002405(9)
    -7217406
    >>> A002405(15)
    -3606726811032345
    """
    return Alef_star(n)


def A002406(n):
    """
    >>> A002406(0)
    1
    >>> A002406(1)
    8
    >>> A002406(3)
    212
    >>> A002406(4)
    -865
    """
    return delta_star(n, n + 1)


def A260780(n):
    """
    >>> A260780(2)
    -1
    >>> A260780(3)
    23
    >>> A260780(7)
    -177
    """
    x, y = triangle_index(n)
    return delta(x, y)


def A260781(n):
    """
    >>> A260781(2)
    1
    >>> A260781(3)
    5
    >>> A260781(7)
    57
    """
    x, y = triangle_index(n)
    return delta_star(x, y)


if __name__ == "__main__":
    sequences = [A002398, A002399, A002400, A002402, A002404, A002406]
    for sequence in sequences:
        print(sequence.__name__)
        print([sequence(i) for i in range(0, 15)])
