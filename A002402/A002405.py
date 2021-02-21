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

