from math import gcd

from polynomial import Polynomial as P


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
    p = L(n-1)
    return (n+1) * p // gcd(n+1, p)


def chi(p, j):
    """
        >>> chi(1, 1)
        -1
        >>> chi(1, 3)
        -7
        >>> chi(2, 4)
        11
    """
    return (-1)**p * A008949(p, j)


def A008949(p, j):
    """
        >>> A008949(5, 5)
        1
        >>> A008949(0, 4)
        16
        >>> A008949(3, 6)
        42
    """
    if p == j:
        return 1
    if p == 0:
        return 2**j
    return A008949(p-1, j-1) + A008949(p, j-1)


def Alef(n):
    """
        This is A002405.
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
    x = a.integral(0, 1) * L(n)
    return int(x + 0.5)


def Alef_star(n):
    """
        This is A002405.
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
    x = a.integral(-1, 0) * L(n)
    return int(x - 0.5)

