# # NumPy ndarrays
#
# Many examples are from the [Numpy documentation](https://numpy.org/doc/stable/user/quickstart.html)

import numpy as np


# ## Create array from list or other sequence
# ### Create 1-dimensional arrays from a sequence

a = np.array([1, 2, 3, 4])
print(a)
print(a.dtype)
print(a.shape)

# ### Create multi-dimensional arrays from nested sequences

b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print(b.dtype)
print(b.shape)

# ### Specify type of array at creation

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(c.dtype)

# ## Create array with specific size and placeholder content
# ### Initial values are 0

d = np.zeros((3, 4))
print(d)
print(d.dtype)
print(d.shape)

# ### Initial values are 1

e = np.ones((2, 3, 4), dtype=np.int16)
print(e)
print(e.dtype)
print(e.shape)

# ### Initial values are not set (values are existing memory content)
#
# Play around with setting a dtype to see resulting initial content.


np.empty((2, 3), dtype='float64')


# ## Create array with range of elements
#
# ### arange() is like built-in range(start, end, step)

np.arange(10, 30, 5)

# ### arange() accepts float arguments

np.arange(0, 2, 0.3)

# ### linspace() is like arange(), but provide num_elements instead of step
# Example returns a 9 element array from 0 to 2, equally spaced


i = np.linspace(0, 2, 9)
print(i)
print(len(i))


# ## Create random array
# For random random numbers, use the `np.random` module.

np.random.random((3, 4))

# To create consistent and reproducible random numbers, create a random number generator (rng) with an initial seed value.

rg = np.random.default_rng(0)   # create default random number generator with seed 0
rg.uniform(-10, 10, size=(2, 3))  # same values every time you run the cell

rg.integers(1, 10, size=(2, 3, 4))


# ## Save and load data from file
#
# ### Save array to .npy file (platform independent)

np.save('numpy_file', i)

# ### Save array to .npy file

j = np.load('numpy_file.npy')
j

# ## Printing
# NumPy displays arrays like nested lists, but with the following layout:
# - the last axis is printed from left to right,
# - the second-to-last is printed from top to bottom,
# - the rest are printed from top to bottom, with each slice separated from the next by an empty line.

as_lists = [
    [
        [
            [f'{i}{j}{k}{l}' for l in range(5)]
            for k in range(4)
        ]
        for j in range(3)
    ] for i in range(2)
]
as_lists

ar = np.array(as_lists)
ar


ar[0, 1, 2, 3]


ar[0][1][2][3]

ar_ints = ar.astype(np.int16)
ar_ints

# ### Array axes

ar_ints.max()  # Max of entire array

ar_ints.max(0)  # Max of axes 0

ar_ints.max(1)  # Max of axes 1

ar_ints.max(2)  # Max of axes 2

ar_ints.max(3)  # Max of axes 3

# ## Methods

k = np.array([
    (1, 2, 3),
    (4, 5, 6)
])
print(k)
print(k.shape)

# ### You can perform calculations on the whole array

print('Sum:', k.sum())
print('Min:', k.min())
print('Max:', k.max())

# ### If you pass an axis in, it calculates over that axis
# For a 2d array, axis 0 is vertical

print('Sum:', k.sum(0))
print('Min:', k.min(0))
print('Max:', k.max(0))

# For a 2d array, axis 1 is horizontal

print('Sum:', k.sum(1))
print('Min:', k.min(1))
print('Max:', k.max(1))

# ### Conversions

k.tolist()

k.astype(str)

# ### Changing shape

k.ravel()

k.reshape((3, 2))

k.T  # Transposed (axes swapped)

# ## Basic operations
#
# Basic operations return a new array, with operation performed on each element
#
# ### Single number operations

l = np.array([10, 20, 30, 40])
l

l - 1

l * 2.5  # (element multiplication)

l ** 2

10 * np.sin(l)

l < 25

# ### 1d array operations
# Operations can be performed against an array of same size

m = np.arange(4)
m

l - m

l * m

l @ m  # 200 (dot product), or

l.dot(m)  # 200 (dot product)


# Operating on an array of a different size will throw an error.

try:
    l - [1, 2]
except Exception as e:
    print(repr(e))

# ### Broadcasting
# For multidimensional arrays, basic operations follow [broadcasting](https://numpy.org/doc/stable/user/basics
# .broadcasting.html) rules:
# - each dimension must either have the same size, or
# - one must have size 1

# ### 2d array operations

n = np.array([(1, 2), (3, 4), (5, 6)])  # (3, 2)
n

o = np.array([[1], [2], [3]])  # (3, 1): 1st dim is same size, 2nd dim size is 1
o

n * o

p = np.array([[1, 2]])  # (1, 2): 1st dim size is 1, 2nd dim is same size
p

n * p

# ### Upcasting
# When arrays have different types, the result will use the more general/precise type

q = np.ones(3, dtype=np.int32)
q

r = np.linspace(0, 1, 3)
r

print(q.dtype)
print(r.dtype)

s = q + r
print(s.dtype)
s

# ### Augmented assignment operations
# These modify the existing array (e.g. +=)

r += q
r

# #### Type errors
# Because arrays have a specific type,
# you may get type errors if you try to store a more precise type in a less precise array

try:
    q += r
except Exception as e:
    print(repr(e))
    print('Cannot store a float64 type into an int32 type array')

# ## Indexing and slicing
# ### 1d arrays
# Works mostly like lists

t = np.arange(5) * 2
t

t[2]

t[1:4]

t[:]

t[::-1]

t[[3, 1, 0]]  # choose specific items (can't do this with lists)

t[::2] = -1  # set every second number to -1 (can't do this with lists)
t

# ### Multidimensional arrays

def f(x, y):
    return 10 * x + y

u = np.fromfunction(f, (5, 4), dtype=int)
u

# #### Nd arrays can have 1 index per axis

u[2, 3]

u[:, 1]

u[1:3, :]

# If fewer axes provided, missing ones are considered complete slices `:`

u[-1]  # equivalent to b[-1, :]

# Can use `...` to fill in empty ones

u[..., -1]  # equivalent to b[:, -1]

# ## Iterating
# Iterating starts at 0 axis

for row in u:
    print(row)

# Can nest to access higher axes

for row in u:
    for item in row:
        print(item)

# Can iterate over each element using ndarray.flat

for item in u.flat:
    print(item)
