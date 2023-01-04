import numpy as np


# 1 DIMENSIONAL ARRAYS

# Index and slice 1d arrays just like lists
a = np.arange(5)*2  # [0, 2, 4, 6, 8]
print(a[2])     # 4
print(a[1:4])   # [2, 4, 6]
print(a[:])     # [0, 2, 4, 6, 8]
print(a[::-1])  # [8, 6, 4, 2, 0]
a[::2] = -1     # set every second number to -1
print(a)        # [-1, 2, -1, 6, -1]


# MULTIDIMENSIONAL ARRAYS

def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]

# Multidimensional arrays can have 1 index per axis
print(b[2, 3])    # 23
print(b[:, 1])    # [1, 11, 21, 31, 41]
print(b[1:3, :])  # [[10, 11, 12, 13], [20, 21, 22, 23]]

# If fewer axes provided, missing ones are considered complete slices (:)
print(b[-1])  # equivalent to b[-1, :] => returns [40, 41, 42, 43]

# Can use ... to fill in
print(b[..., -1])  # equivalent to b[:, -1] => returns [3, 13, 23, 43]


# ITERATING

# Iterating starts at 0 axis
for row in b:
    print(row)

# Can nest to access higher axes
for row in b:
    for item in row:
        print(item)

# Can iterate over each element using ndarray.flat
for item in b.flat:
    print(item)