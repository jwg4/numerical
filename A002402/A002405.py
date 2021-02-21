from math import gcd, factorial

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


def L_factorial(n):
    """
        >>> L_factorial(6)
        302400
    """
    return L(n) * factorial(n)


def gamma(p, j):
    """
        >>> gamma(1, 1)
        -1
        >>> gamma(1, 3)
        -3
        >>> gamma(2, 4)
        6
    """
    return (-1)**p * choose(p, j)


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
    return round(x)


def Alef_star(n):
    """
        This is A002405.
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
    x = a.integral(-1, 0) * L(n)
    return round(x)


def A(n, m):
    """
        >>> A(1, 3)
        36
        >>> A(2, 3)
        6
    """
    return L_factorial(m) // L_factorial(n)


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
    return sum(gamma(p, j) * A(j, J) * Alef(j) for j in range(p, J+1))


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
    return sum(gamma(p, j) * A(j, J) * Alef_star(j) for j in range(p, J+1))


def delta_sum(J):
    return sum(delta(p, J) for p in range(0, J+1))


if __name__ == '__main__':
    print("A002398")
    print(", ".join(str(delta(0, J)) for J in range(0, 10)))
    print(", ".join(str(delta_sum(J)) for J in range(0, 10)))
    print(", ".join(str(L_factorial(J)) for J in range(0, 10)))

