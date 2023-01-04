"""
Creating arrays examples from the Numpy documentation
https://numpy.org/doc/stable/user/quickstart.html#array-creation
"""
import numpy as np


# CREATE ARRAY FROM LIST OR OTHER SEQUENCE

# Create 1-dimensional arrays from a sequence
a = np.array([1, 2, 3, 4])  # 1-dimensional array
print(f'a: {a}')
print(a.dtype)  # dtype('int64')
print(a.shape)

# Create multi-dimensional arrays from nested sequences
b = np.array([(1.5, 2, 3), (4, 5, 6)])  # 2-dimensional array
print(f'b: {b}')
print(b.dtype)  # dtype('float64')
print(b.shape)

# Specify type of array at creation
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(f'c: {c}')
print(c.dtype)  # dtype('complex128')


# CREATE ARRAY WITH SPECIFIC SIZE AND PLACEHOLDER CONTENT

# Initial values are 0
d = np.zeros((3, 4))
print(f'd: {d}')
print(d.dtype)  # dtype('float64')

# Initial values are 1
e = np.ones((2, 3, 4), dtype=np.int16)
print(f'e: {e}')
print(e.dtype)  # dtype('int16')

# Initial values are not set (values are existing memory content)
f = np.empty((2, 3))
print(f'f: {f}')
print(f.dtype)  # dtype('float64')


# CREATE ARRAY WITH RANGE OF ELEMENTS

# arange is like built-in range(start, end, step)
g = np.arange(10, 30, 5)  # [10, 15, 20, 25]
print(f'g: {g}')

# arange accepts float arguments
h = np.arange(0, 2, 0.3)  # [0., 0.3, 0.6, 0.9, 1.2, 1.5, 1.8]
print(f'h: {h}')

# linspace is like arange, but provide num_elements instead of step
i = np.linspace(0, 2, 9)  # returns a 9 element array from 0 to 2, equally spaced
print(f'i: {i}')
print(len(i))


# CREATE RANDOM ARRAY

rg = np.random.default_rng(0)   # create instance of default random number generator (with seed 0)
j = rg.random((2, 3))  # array of size (2, 3) with random floats between 0 and 1
print(f'j: {j}')

k = rg.integers(1, 10, (2, 3, 4))  # array of size (2, 3, 4) with random integers between 1 and 10
print(f'k: {k}')


# SAVE AND LOAD DATA FROM FILE

# Save array to .npy file (platform independent)
np.save('numpy_file', i)

# Save array to .npy file
h = np.load('numpy_file.npy')
print(f'h: {h}')
