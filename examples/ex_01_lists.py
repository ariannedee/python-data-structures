# # Lists
# ## Brief summary of Python lists
# ### Creating lists

list()

['a', 'b', 1, 2]

list('12345')

list({'hello': 'world', 'foo': 'bar'})  # Only takes keys

# You can also build lists using **list comprehensions**

[2 ** i for i in range(12)]

# We will look more at list comprehensions in the second hour of the class.

# ## Slicing and indexing lists
# These also work on any sequence (tuple, string, bytearray, etc)
#
# ### Getting an item via index (indexing)
# The format is `sequence[index]`
#
# Indices start at `0` and go to `len(sequence) - 1`.

sequence = list('abcde')
sequence

sequence[0]

end = len(sequence) - 1
sequence[end]

try:
    sequence[100]
except IndexError as e:
    repr(e)

# You can also go from the end of the list at `-1` to the beginning at `-len(sequence)`

sequence[-1]

beginning = -len(sequence)
sequence[beginning]

# ### Getting a sublist (slicing)
#
# The format is `sequence[start:stop:step]`
#
# This will return a new sequence with items starting at `start`, ending at `stop - 1`, and skipping `step` each time.
#
# `step` is optional, and the default is `1`.
#
# If a number is missing, its value is assumed to be either beginning or end of the list, depending on the context.

sequence[1:3]  # indices 1 and 2

sequence[:4]  # beginning (0 to 3

sequence[2:]  # 2 to end (4

sequence[:]  # full list

sequence[::2]  # every second item

sequence[2::-1]  # 2, 1, 0

sequence[::-1]  # reversed

# ## Updating contents

sequence[0] = 'new'  # update existing item
sequence

del sequence[-1]  # deleting by index
sequence

sequence.append('end')  # add item to the end
sequence

sequence.insert(1, 'a')  # add item at index
sequence

# ## Checking containment

'e' in sequence

'a' in sequence

# ## Looping

for value in sequence:
    print(value * 2)

# If you need the index as well, use `.enumerate()`

for i, value in enumerate(sequence):
    print(f'{i}: {value}')
