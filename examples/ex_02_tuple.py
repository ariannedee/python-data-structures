# # Tuples
#
# Immutable (non-modifiable) lists.
#
# ## Creating tuples

a = (1, 2, 3)
a

# Be careful with single item tuples. 
#
# They need a trailing comma or else it's just an expression.

b = ('Hello',)
b

c = ('Goodbye')
c

# ## Cannot update tuples

try:
    b[0] = 'Howdy'
except Exception as e:
    print(repr(e))

# ## Slicing and indexing
#
# It's done just like lists!
#
# ## Packing and unpacking
#
# **Packing** happens when you don't include the parentheses

coords = 1.2, 3.4
coords

# **Unpacking** happens when you expand a `tuple` into multiple variables

lat, lon = coords
print(lat)
print(lon)

# ## When to use tuples

# ### Representing objects/heterogeneous data

blue = 0, 0, 255
colours = ['red', 'green', blue]

# ### Swap variable names
#
# Use `tuple` packing and unpacking to do neat stuff.
#
# Without it, you'd need to introduce a temporary 3rd variable.

# +
d = 100
e = -100

d, e = e, d
print(d)
print(e)
# -

# ### Represent constants/immutable values

paris = (33.66, -95.54)
athens = (32.20, -95.85)

# ### Use as dict keys

texas_cities = {
    paris: 'Paris',
    athens: 'Athens'
}
texas_cities


# ### Return multiple values from a function

# +
def div_mod(x, y):
    div = x // y
    mod = x % y
    return div, mod

quotient, remainder = div_mod(11, 2)
print(f'11/2 is {quotient} remainder {remainder}')
# -

# **Note**: the builtin `divmod()` exists because the CPU can determine them at the same time, so it saves computing time if you need both.

# ### Access multiple items in a loop
#
# When you access multiple variables in `for` loops, you're actually unpacking a `tuple`.

for i, val in enumerate('abc'):
    print(f'{i}: {val}')

for tup in enumerate('abc'):
    print(tup)

# ### The zip() function
#
# If you want to loop over items two or more sequences simultaneously, you can zip them and loop over the results.

# +
nums = [1, 2, 3]
letters = ['a', 'b', 'c']

print(list(zip(nums, letters)))

for num, letter in zip(nums, letters):
    print(num * letter)
# -

# ### Practical uses of zip()
#
# Copied from this [Real Python](https://realpython.com/python-zip-function/) article
#
# #### Calculating in pairs
#
# If you have a spreadsheet of `total_sales` and `costs` for multiple months, you can calculate the `profit` for each month and for the whole period.

# +
total_sales_q2 = [52000.00, 51000.00, 48000.00]
costs_q2 = [46800.00, 45900.00, 43200.00]

profit_q2 = 0
for sales, costs in zip(total_sales_q2, costs_q2):
    profit = sales - costs
    print(f'Profit: ${profit}')
    profit_q2 += profit

print(f'Total profit: ${profit_q2:,}')
# -

# #### Building dictionaries

# +
fields = ['name', 'last_name', 'age', 'job']
values = ['Jasmine', 'Doe', '45', 'Python Developer']

person = dict(zip(fields, values))
person
