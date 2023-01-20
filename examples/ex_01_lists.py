# # Lists
#
# ## Brief summary of Python lists
#
# ### Creating lists

# +
empty_list_1 = []
empty_list_2 = list()

list_with_contents = ['a', 'b', 1, 2]

from_sequence = list('12345')
from_sequence
# -

from_dict = list({'hello': 'world', 'foo': 'bar'})
from_dict

# You can also build lists using **list comprehensions**

powers_of_2 = [2 ** i for i in range(12)]
powers_of_2

# We will look more at list comprehensions in the second hour of the class.

# ## Slicing and indexing lists
# These also work on any sequence (tuple, string, bytearray, etc)
#
# ### Getting an item via index (indexing)
#
# The format is `sequence[index]`
#
# Indices start at 0 and go to `len(sequence) - 1`.

sequence = list('abcde')
sequence

print(f'0: {sequence[0]}')
end = len(sequence) - 1
print(f'{end}: {sequence[end]}')

try:
    sequence[100]
except IndexError as e:
    repr(e)

# You can also go from the end of the list at `-1` to the beginning at `-len(sequence)`

print(f'-1: {sequence[-1]}')
beginning = -len(sequence)
print(f'{beginning}: {sequence[beginning]}')

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

# ## Looping

for item in sequence:
    item * 2

# ## List implementation
#
# (In CPython)
#
# Lists in Python store:
# 1. The size of the list
# 2. An array of pointers
# 3. Values contained in the list (pointed to by an item in the above array)
#
# When you **update** the value at an index:
# 1. The new value is stored
# 2. The pointer at that index is updated to the new location
#
# When you **append** a new item, Python:
# 1. Increases the size of the list by 1
# 2. Stores the new item value
# 3. Adds a pointer to the array of pointers
#
# **Note about appends**: So that Python doesn't have to update the size of the pointer array all the time, more space is allocated than is needed. Then when all spaces are filled, the array expands again. Therefore, some appends will take longer than others.
#
# If you **insert** an item at an index, it is the same as appending, except in step 3, the array has to move pointers around so the new pointer can be inserted at the proper location.
#
# If you **delete** an item, unless it's at the end, the array has to move pointers around to fill in the empty spot.

# ### Time complexity of operations
#
# **Fast**:
# - Updating existing item
# - Appending to the end
#
# **Slow**:
# - Deleting an item
# - Inserting at an index
# - Checking containment
