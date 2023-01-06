import numpy as np
import pandas as pd

# CREATING SERIES FROM ARRAY

# index: must be same size as array
a = pd.Series([1, 3, 5, 7], index=['a', 'c', 'd', 'b'])
print(f'\n- a -\n{a}')

# No index: default integer index starting at 0
b = pd.Series([1, 3, 5, np.nan, 6, 8])
print(f'\n- b -\n{b}')


# CREATING SERIES FROM DICT

# No index: use keys
c = pd.Series({"b": 1, "a": 0, "c": 2})
print(f'\n- c -\n{c}')

# index: pull corresponding values from data
d = pd.Series({"b": 1, "a": 0, "c": 2}, index=["b", "d", "c"])
print(f'\n- d -\n{d}')


# CREATING SERIES FROM SCALAR

# index (required): set every value to data value
e = pd.Series(2, index=["a", "b", "c"])
print(f'\n- e -\n{e}')
