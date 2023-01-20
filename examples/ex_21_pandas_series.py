# # Working with Pandas Series
#
# ## Creating Series

import numpy as np
import pandas as pd

# ### From array
#
# #### `index`: must be same size as `ndarray`/`list`

a = pd.Series([1, 3, 5, 7], index=['a', 'c', 'd', 'b'])
a

# #### No `index`: default integer index starting at 0

b = pd.Series([1, 3, 5, np.nan, 6, 8])
b

# ### From dict
#
# #### No `index`: use keys

c = pd.Series({"b": 1, "a": 0, "c": 2})
c

# #### `index`: pull corresponding values from data

d = pd.Series({"b": 1, "a": 0, "c": 2}, index=["b", "d", "c"])
d

# ### From scalar
#
# #### `index` (required): set every value to data value

e = pd.Series(2, index=["a", "b", "c"])
e

# ## Working with Series
#
# ### Series is ndarray-like
#
# `Series` acts similarly to a `ndarray` and is a valid argument to most NumPy functions.
# Operations such as slicing will also slice the index.

f = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
f

f[0]

f[:2]

f[f > f.median()]

f[[4, 3, 1]]

np.exp(f)

# ### Series is dict-like
#
# You can get and set values by index label.

f['a']

f['a'] = 100
f

try:
	f['f']
except KeyError as e:
	print(repr(e))

f.get('f', np.nan)

f.a

# ## Working with `Series`
#
# ### Vector operations
#
# You can do operations on a `Series` similar to working with `ndarray`.

f + f

f * 3 + [0, 0.25, 0.5, 0.75, 1] - 1

# When operating with non-`Series` sequences, the length must match.
#
# ### Label alignment
#
# `Series` automatically align the data based on label.

g = pd.Series(.5, index=['b', 'c', 'e', 'f'], name='g')
f + g

# ## `name` attribute
#
# You can label any `Series` with a `name`

s = pd.Series(np.random.randn(5), name="random series")
s

s.name

# In a `DataFrame`, the `Series` name will be the column label.
#
# ### Renaming
#
# You can change the name of a `Series` by setting the `name` attribute.

s.name = 'Series 1'
s

# Use the `rename()` method to create a copy with a new name.

s2 = s.rename('Series 2')
s2

s


