# Variables region
import math

h = 0.01
a = h
b = 1


# end

# Functions region

def u(_x):
    return math.sin(_x ** 2 / 2)


def du(_x):
    return a * math.cos(_x ** 2 / 2)


def d2u(_x):
    return (-1) * _x ** 2 * math.sin(_x ** 2 / 2) + math.cos(_x ** 2 / 2)


def f1(_u2):
    return _u2


def f2(_x, _u1, _u2):
    return _u2 / _x - _x ** 2 * _u1
# end
