# # collections.OrderedDict

from collections import OrderedDict

# ## Create
# ### Empty dict

a = OrderedDict()
a

# ### From a dict

b = OrderedDict({1: 'a', 2: 'b'})
b

# ### From a sequence
# Each item in the sequence must be another sequence with length 2

c = OrderedDict([['a', 'apple'], {'b', 'banana'}, ('c', 'cherry')])
c

# ## Use like a dictionary
# `OrderedDict` has all the same methods as `dict`.

b[0] = 'z'
b

for i in range(4):
    print(b.get(i, 'Not found'))

# ## Iteration order
# When iterating, it retains memory of insertion order

for key, value in b.items():
    print(f'{key}: {value}')

# ## Pop item
# Additional method to remove the last key-value pair and return it.

b.popitem()

b

# ## Reorder items
# `.move_to_end(key, last=True)` will move the item with `key` either to the end (`last=True`) or the front (`last=False`).

b.move_to_end(1)
b

try:
    b.move_to_end(0, last=False)
except Exception as e:
    print(repr(e))

for key, value in b.items():
    print(f'{key}: {value}')

# ## When to use OrderedDict over dict
# `dict` is has been ordered since Python3.6.
#
# You should still use `OrderedDict` to:
# - Clearly state that the order is important
# - Use the `.move_to_end()` method
# - Test dictionary equality based on order
# - Maintain backwards compatibility with Python < 3.6
