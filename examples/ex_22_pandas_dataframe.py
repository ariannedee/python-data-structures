# # Working with Pandas DataFrames

import numpy as np
import pandas as pd

# ## Creating DataFrames
#
# Can be created from:
# - Dict of 1D ndarrays, lists, tuples, dicts, or Series
# - List of dicts
# - 2-D ndarray
# - [Structured or record](https://numpy.org/doc/stable/user/basics.rec.html) ndarray
# - A Series
# - Another DataFrame
# - CSV, Excel, SQL or JSON file
# - A list of namedtuples
# - A list of dataclasses (v1.1.0+)

dict_of_lists = {"A": [1.0, 2.0, 3.0, 4.0], "B": [4.0, 3.0, 2.0, 1.0]}
pd.DataFrame(dict_of_lists)

dict_of_dicts = {"C": {100: 1, 101: 2, 102: 3}, "D": {100: 'abc', 101: 'def', 102: 'ghi'}}
pd.DataFrame(dict_of_dicts)

# Subset of data from the 2022 Stack Overflow Developer Survey
df = pd.read_csv('languages.csv')
df

# ## Working with columns
#
# A `DataFrame` is like a `dict` that contains `Series` objects with the same index.
#
# We can can get, set and delete columns as if they were in a `dict`.

df['Name']  # Getting a column

df['Percent not used'] = 100 - df['Percent used']  # Add a new column
df

not_used = df.pop('Percent not used')  # Removes and returns the column
not_used

df.plot(kind='bar', x='Name')

# ## Example: Plotting over years
#
# ### Update the dataframe so the 'Percent used' is multiple columns based on year

df.rename(columns={'Percent used': '2022'}, inplace=True)
df

# ### Add more years of data
#
# Randomly update the percent used from the previous year by +-5

# +
from random import random

for year in range(2021, 2017,  -1):
    df[str(year)] = df[str(year+1)] + [(round(random(), 3) * 10 - 5) for i in range(4)]
df
# -

df.index = df.pop('Name')
df

df.sort_index(axis='columns', inplace=True)
df

df.plot.bar()

df2 = df.T
df2

df2.plot()


