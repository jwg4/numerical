Consider the ordinary differential equation of the first order

y' = f(y, x)

which is to be integrated step by step over 
>>> a, b, h = -1.0, 1.5, 0.01
>>> range(a, b, h)

A natural method for accomplishing this integration is a predictor-corrector process based on a suitable finite difference interpolating formula.

Let 
>>> x0 = a + J * h
and assume that y is known at the points 
>>> x = dict()
>>> for j in range(0, J + 1):
...     x[j] = x0 - j * h

One can then write for y' the approximation to it which is provided by the Gregory-Newton backward interpolating formula.
