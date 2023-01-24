# # Sets
# Sets are a collection that:
# - have no order
# - cannot contain duplicates
# - cannot access individual items (except by iterating over)
#
# ## Brief summary of Python sets
# ### Creating sets

set()

{'a', 'b'}

set((1, 2, 1, 3))  # pass any iterable in

# You can also build sets using **set comprehensions**

{2 ** i for i in range(0, 10, 2)}

# We will look more at set comprehensions in the second hour of the class.

# ### Valid set values
# `set` **elements** must be __hashable__. Basically, if it's a builtin type, it can't be mutable (like `list`,
# `dict` or `set`). If it's a custom class, it must implement a special method for hashing and checking equality.
#
# Elements use `==` to determine key equality. So `1`, `1.0` and `True` all map to the same element.

{True, 1, 1.0, '1', (1,)}

try:
    {[1, 2]}
except Exception as e:
    print(repr(e))

# ## Updating contents

s = {1, 2}

s.add(3)
s

s.add(1)  # Already exists, so no change
s

s.update([1, 2, 3, 4])
s

s.update({1: 'a', 5: 'e'})  # Only adds keys
s

s.remove(1)  # element must be in set
s

try:
    s.remove(-1)
except Exception as e:
    print(repr(e))

s.discard(5)  # element doesn't need to be in set
s

s.discard(-1)  # no error thrown

# ## Getting contents
# You can `.pop()` a random element from the set. There's no way of accessing a specific item.

s.pop()

s

# ## Checking containment

s = {1, 2}

# ### Of an element

1 in s

3 in s

# ### Of another set
# `.issuperset(other)`: does __set__ fully contain __other__

s.issuperset({2,})

s.issuperset({2, 3})

# `.issubset(other)`: does __other__ fully contain __set__

s.issubset({1, 2, 3,})

s.issubset({2, 3})

# `.isdisjoint()`: are there no common elements between __set__ and __other__

s.isdisjoint({3, 4})

s.isdisjoint({2, 3})

# ## Looping
# Sets have an undefined order.

for element in {'a', 'b', 'c'}:
    print(element)

# ## Set operations
# You can do most set operations via methods or operators.

odd = {1, 3, 5}

prime = {2, 3, 5}

# ### Union
# All elements in either A or B

odd.union(prime)

odd | prime

# ### Intersection
# All elements in both A and B

odd.intersection(prime)

odd & prime

# ### Difference
# Elements in A but not B

odd.difference(prime)

prime.difference(odd)

odd - prime

prime - odd

# ### Symmetric difference
# Elements in either A or B but not both

odd.symmetric_difference(prime)

odd ^ prime
