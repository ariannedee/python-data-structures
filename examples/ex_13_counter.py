# # collections.Counter
# Also called a multiset or bag, `Counter` keeps track of how many times an element is included in a set.

from collections import Counter

coins = Counter()
coins.update(['silver', 'silver', 'gold'])
coins.update({'copper': 4, 'silver': 2})
coins

# It's like a specialized `dict`, where the **key** is an element and the **value** is an integer of counts.
# ## Creating counters 
# ### From a sequence
# If the sequence can contain duplicates, like `list` or `tuple`, it will keep track of item counts

a = Counter([1, 1, 3, 2, 1, 3, 4, 1])
a

# Sets remove duplicates when created, each count will be 1.

b = Counter({1, 1, 3, 2, 1, 3, 4, 1})
b

# ### From a dictionary
# It will treat `{key: value}` as `{element: count}`

c = Counter({'a': 2, 'b': 5, 'c': 1})
c

# If your dictionary _values_ are not all `int`s, some methods will work, and others will give you errors.

d = Counter({'a': 2, 'b': 'hi', 'c': 1.})
d.update('c')
d

try:
    d.update('b')
except Exception as e:
    print(repr(e))

# ## Updating
# You can pass in a sequence or dict of counts.


e = Counter()
e

# `.update()` to adds items (uses the `+` operator)

e.update('abbb')
e

e.update({'c', 'c', 'a'})  # c is only counted once in a normal set
e

e.update({'c':-3, 'd': 2})
e

# `.subtract()` removes items (uses the `-` operator)

e.subtract('abbb')
e

e.subtract({'a': -3, 'b': 3})
e

# ## Counters are like dictionaries

e['a']

e.get('d', 0)

e.get('e', 0)

e['c'] = 1

for key, value in e.items():
    print(f'{key}: {value}')

# ## Special Counter methods
# `.elements()` is an iterator of all the elements, repeating each value as many times as its count

for element in e.elements():  # negative integer counts won't be included
    print(element)

# `.elements()` expects all counts to be integers

e['c'] = 1.0
e

try:
    for value in e.elements():
        print(value)
except Exception as ex:
    print(repr(ex))

# `.most_common()` will return a list of the most common elements as `(element, count)`. If you pass an integer `n`, only that number are returned.

e.most_common()

e.most_common(2)
