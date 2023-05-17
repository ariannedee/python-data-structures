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

df = pd.read_csv('languages.csv')  # Subset of data from the 2022 Stack Overflow Developer Survey
df

# ## Index and columns

df.index

df.columns

df.index += 100  # Update index
df

# ## Working with columns
#
# A `DataFrame` is like a `dict` that contains `Series` objects with the same index.
#
# We can can get, set and delete columns as if they were in a `dict`.

df['Name']  # Getting a column

# For column names that are valid Python variables names, you can access them like attributes

df.Name  # Get column as attribute

df['Percent not used'] = 100 - df['Percent used']  # Add a new column
df

# ## Getting rows
#
# Returns a `Series`

df.loc[100]  # By label

df.iloc[2]  # By position

# ## Getting data (indexing)
#
# Returns data in a cell

df.loc[102, 'Name']  # By label

df.iloc[3, 2]  # By position

# ## Slicing
#
# Returns a `DataFrame`

df.iloc[:3, :2]

df.iloc[:, [0]]  # Note: without [0] in brackets, it would return a Series

df.loc[101:102]  # Note: with loc, end is inclusive

df.loc[[101, 103]]

df.loc[:, ['Name', 'Percent not used']]

# ### Boolean indexing

df['Percent used'] > 50

df[df['Percent used'] > 50]

# ## Plotting
#
# ### Example 1 - simple bar chart
#
# Let's create a bar chart mapping Percent used (y) to Name (x)
#
# #### Create a custom view of the data
#
# Index is x-axis and column is y-axis.

df2 = df.iloc[:, :2]
df2

df2.index = df2.pop('Name')
df2

# #### Specify the kind of plot (bar) and customize the x and y axis if necessary

df2.plot.bar()

# ### Example 2: Plotting over years
#
# #### Update the dataframe to track percent used over multiple years

df3 = df2.rename(columns={'Percent used': '2022'})
df3

# #### Add more years of data
#
# Randomly update the percent used from the previous year by +-5

# +
from random import uniform

for year in range(2021, 2017,  -1):
    df3[str(year)] = df3[str(year+1)] + [round(uniform(-5, 5), 2) for i in range(4)]
df3
# -

df3 = df3.sort_index(axis='columns')
df3

df3.plot.bar()

df4 = df3.T
df4

df4.plot()
