# # Dict Comprehensions
# Just like list comprehensions, but use a different syntax to create dicts.
# ## Basic comprehsions
# Format: `{key_exp: value_exp for member in iterable}`

powers_of_2 = {i: 2**i for i in range(2, 10, 2)}
powers_of_2

# ### As for-loop

# +
powers_of_2 = {}
for i in range(2, 10, 2):
    powers_of_2[i] = 2**i

powers_of_2
# -

# ## Using conditionals

# +
phrase = "peter piper picked a peck of pickled peppers"
letter_set = set(phrase)

letter_counts = {char: phrase.count(char) for char in letter_set if char != ' '}
letter_counts
# -

# ### As for-loop

# +
phrase = "peter piper picked a peck of pickled peppers"
letter_set = set(phrase)

letter_counts = {}
for char in letter_set:
    if char != ' ':
        letter_counts[char] = phrase.count(char)

letter_counts
# -

# ## With ternary operator

is_even = {i: True if i % 2 == 0 else False for i in range(10)}
is_even

is_even = {}
for i in range(10):
    if i % 2 == 1:
        is_even[i] = True
    else:
        is_even[i] = False
is_even

# ## Nested comprehensions
# ### Dict wth list values

lesser_nums = {
    i: [j for j in range(i)] for i in range(10)
}
lesser_nums

# ### As for-loop

lesser_nums = {}
for i in range(10):
    nums = []
    for j in range(i):
        nums.append(j)
    lesser_nums[i] = nums
lesser_nums

# ### Flat nesting

products = {(x, y): x*y for x in range(3) for y in range(3)}
products

# ### As for-loop

products = {}
for x in range(3):
    for y in range(3):
        products[(x, y)] = x * y
products
