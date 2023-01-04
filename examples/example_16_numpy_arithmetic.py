"""
https://numpy.org/doc/stable/user/quickstart.html#basic-operations
"""
from math import pi

import numpy as np
from numpy.core._exceptions import UFuncTypeError


# Basic operations return a new array, with operation performed on each element

print("Single number operations")
a = np.array([10, 20, 30, 40])
print(f'a: {a}')
print(a - 1)  # [9, 19, 29, 39]
print(a * 2.5)  # [25., 50., 75., 100.] (element multiplication)
print(a ** 2)  # [100, 400, 900, 1600]
print(10 * np.sin(a))  # [-5.44021111, 9.12945251, -9.88031624,  7.4511316]
print(a < 25)  # [True, True, False, False]
print()


# Operations can be performed against an array of same size

print("1d array operations")
b = np.arange(4)  # [0, 1, 2, 3]
print(f'b: {b}')
print(a - b)  # [10, 19, 28, 37]
print(a * b)  # [0, 20, 60, 120] (element multiplication)
print(a @ b)  # 200 (dot product), or
print(a.dot(b))  # 200 (dot product)
print()


# For multidimensional arrays, basic operations follow broadcasting rules:
# each dimension must either have the same size, or one must have size 1
# https://numpy.org/doc/stable/user/basics.broadcasting.html

print("2d array operations")
c = np.array([(1, 2), (3, 4), (5, 6)])  # (3, 2)
print(f'c: {c}')

d = np.array([[1], [2], [3]])  # (3, 1): 1st dim is same size, 2nd dim size is 1
print(f'd: {d}')
print(f'c*d: {c * d}')

e = np.array([[1, 2]])  # (1, 2): 1st dim size is 1, 2nd dim is same size
print(f'e: {e}')
print(f'c*e: {c*e}')
print()


# Augmented assignment operations (e.g. +=) modify the existing array

print("Augmented assignment operations")
print(f'a: {a}')  # [10, 20, 30, 40]
a *= 3
print(f'a: {a}')  # [30, 60, 90, 120]

try:
    a += 0.5  # Raises a type error because "a" stores integers
except UFuncTypeError:
    print("Cannot store a float64 in an int64 array")
print()


# When arrays have different types, the result will use the more general/precise type (upcasting)

print("Type upcasting")
f = np.ones(3, dtype=np.int32)  # [1, 1, 1]
g = np.linspace(0, 1, 3)        # [0., 0.5, 1.]
print(f.dtype)                  # 'int32'
print(g.dtype)                  # 'float64'
h = f + g
print(f'h: {g}')  # [1., 2.57079633, 4.14159265]
print(h.dtype)    # 'float64'

i = h + 1j
print(f'i: {i}')  # [1.+1.j, 1.5+1.j, 2.+1.j]
print(i.dtype)    # 'complex128'
print()
