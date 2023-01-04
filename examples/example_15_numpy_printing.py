"""
NumPy displays arrays like nested lists, but with the following layout:
- the last axis is printed from left to right,
- the second-to-last is printed from top to bottom,
- the rest are printed from top to bottom, with each slice separated from the next by an empty line.
"""
import numpy as np

ar = [
    [
        [
            [f'{i}{j}{k}{l}' for l in range(5)]
            for k in range(4)
        ]
        for j in range(3)
    ] for i in range(2)
]
ar = np.array(ar)

print(ar)
print(ar[0, 1, 2, 3])
x = ar.astype(int)
print(x)
print(x.dtype)
print(x.max(0))