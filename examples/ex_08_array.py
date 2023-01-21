# # array.array
# [Documentation](https://docs.python.org/3/library/array.html)

import array

# Must declare the type of data it holds:
# - `'f'` - float
# - `'i'` - integer
# - `'u'` - Unicode character
#
# More types in [documentation](https://docs.python.org/3/library/array.html)

arr_f = array.array("f", (1.0, 1.5, 2.0, 2.5))
arr_f

# ### Arrays have many similar list methods

arr_f.append(3.0)
arr_f

arr_f.insert(0, 0.5)
arr_f

arr_f.reverse()
arr_f

# ### And a few conversion methods

arr_f.tolist()

arr_f.tobytes()

# ### Working with files

# You can save arrays to a file as bytes, so use binary `'b'` mode. 

with open('array', 'wb') as file:
    arr_f.tofile(file)

arr_f2 = array.array("f", (-1.0, -1.5))
arr_f2

# `.fromfile(file, n)` appends `n` items from the file onto the existing array.

with open('array', 'rb') as file:
    arr_f2.fromfile(file, 3)
arr_f2

# ## Working with chars
# The `'u'` type stores Unicode characters and prints them like a string (instead of list).

arr_u = array.array('u', 'I 💚 🐍')
arr_u

arr_u.append('!')
arr_u

as_u = arr_u.tounicode()  # Only works with 'u' type
print(type(as_u))
print(as_u)

# ## Size specific integers
# In most other languages, integers have a minimum and maximum value.
# Python increases the memory for integers dynamically behind the scenes, so there is no minimum or maximum value.
#
# Since arrays assign a fixed amount of memory for each item, you must specify the number of bytes allocated for integers arrays and whether or not they can store negative numbers (signed vs unsigned).
#
# Type to byte list:
# - `'b'` and `'B'` (char): 1 byte
# - `'h'` and `'H'` (short): 2 bytes
# - `'i'` and `'I'` (int): 2 bytes
# - `'h'` and `'H'` (long): 4 bytes
# - `'l'` and `'L'` (long long): 8 bytes
# - `'d'` (double): 8 bytes
#
# ### 'B': unsigned char
# This is an unintuitive name. It's basically 1 byte of data as an integer

smallest = 0
largest = 2**8 - 1
arr_B = array.array("B", (smallest, largest))
arr_B

try:
    arr_B.append(largest + 1)
except Exception as e:
    print(repr(e))

try:
    arr_B.append(smallest - 1)
except Exception as e:
    print(repr(e))

# ### 'b': signed char
# Like unsigned char but one bit is used to store the sign.

smallest = -(2**7)
largest = 2**7 - 1
arr_f2 = array.array("b", (smallest, largest))
arr_f2

try:
    arr_f2.append(largest + 1)
except Exception as e:
    print(repr(e))

# ### 'I': unsigned int
# 2 bytes

smallest = 0
largest = 2**32 - 1
arr_I = array.array("I", (smallest, largest))
arr_I

try:
    arr_I.append(largest + 1)
except Exception as e:
    print(repr(e))

try:
    arr_I.append(smallest - 1)
except Exception as e:
    print(repr(e))

# ### 'i': signed integer
# 2 bytes, with 1 bit to store the sign

smallest = -(2**31)
largest = 2**31 - 1
arr_i = array.array("i", (smallest, largest))
arr_i

try:
    arr_i.append(largest + 1)
except Exception as e:
    print(repr(e))

try:
    arr_i.append(smallest - 1)
except Exception as e:
    print(repr(e))
