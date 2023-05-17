# # Dicts
# Dictionaries are a type of key-value mapping object.
#
# Instead of accessing items by index (position), we get them through via keys.
# ## Creating dicts

dict()

{'a': 1, 'b': 2}

dict(((1, 2), (3, 4)))  # Must be a sequence of 2-item lists/tuples

# You can also build dicts using **dict comprehensions**

{i: 2 ** i for i in range(0, 10, 2)}

# We will look more at dict comprehensions in the second hour of the class.

# ### Valid dict types
# `dict` **values** can be anything.
#
# `dict` **keys** must be __hashable__. Basically, if it's a builtin type, it can't be mutable (like `list`, `dict` or `set`). If it's a custom class, it must implement a special method for hashing and checking equality.
#
# Keys use `==` to determine key equality. So `1`, `1.0` and `True` all map to the same key.

{
    'a': True, 
    1: ['a', 2,],
    True: False,
    None: {}, 
    1.0: 'float',
    (1, 2): 'tuple',
}

try:
    {[1, 2]: 'list'}
except Exception as e:
    print(repr(e))

# ## Getting and updating contents

d = {'a': 1, 'b': 2}

# ### Getting values
# We get items by key and not index (even if it's an int)

d['a']

try:
    print(d['c'])  # Key doesn't exist
except Exception as e:
    print(repr(e))

d.get('a')

print(d.get('c'))  # Key doesn't exist

d.get('c', 'Not found')  # Can provide default value

# ### Updating values

d['a'] = 'new'  # update existing item
d

d['c'] = 3  # add item a new item
d

del d['b']  # deleting by key
d

# ## Checking containment
# Checks keys, not values

'a' in d

'e' in d

# ## Looping
# Basic loop is over keys

for key in d:
    print(key)

# It's recommended to use `.keys()`, `.values()` or `.items()` to be explicit about what you're looping over.

for key, value in d.items():
    print(f"{key}: {value}")
