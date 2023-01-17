# # List Comprehensions
#
# ## Basic comprehsions

squares = [i ** 2 for i in range(10)]
squares

# ### As for-loop

# +
squares = []
for i in range(10):
    squares.append(i ** 2)

squares
# -

# ## Using conditionals

evens = [i for i in range(10) if i % 2 == 0]
evens

# ### As for-loop

# +
evens = []

for i in range(10):
    if i % 2 == 0:
        evens.append(i)
evens
# -

# ## With ternary operator

is_even = [True if i % 2 == 0 else False for i in range(10)]
is_even

is_even = []
for i in range(10):
    if i % 2 == 1:
        is_even.append(True)
    else:
        is_even.append(False)
is_even

# ## Nested comprehensions
#
# ### Nested lists

coords = [
    [(x, y) for y in range(3)] for x in range(3)
]
coords

# ### Looping over coords

for row in coords:
    print(row)

# ### As for-loop

coords = []
for x in range(3):
    row = []
    for y in range(3):
        row.append((x, y))
    coords.append(row)
coords

# ### Flattened list

coords = [(x, y) for x in range(3) for y in range(3)]
coords

# ### As for-loop

coords = []
for x in range(3):
    for y in range(3):
        coords.append((x, y))
coords

# ## Complex comprehension example

num_lists = [[7, 2], [6], [1, 4, 5], [-2, 8, 0]]

small_nums = [num
    for nums in num_lists
    for num in nums
    if num < 5]
small_nums

# ### As for-loop

small_nums = []
for nums in num_lists:
    for num in nums:
        if num < 5:
            small_nums.append(num)
small_nums

# ## Very complex example

num_lists = [[7, 2], [6], [1, 4, 5], [-2, 8, 0]]

a_list = [num if num > 3 else -num
    for nums in num_lists
    if len(nums) > 1
    for num in nums
    if num % 2 == 1]
a_list

# ### As for-loop

a_list = []
for nums in num_lists:
    if len(nums) > 1:
        for num in nums:
            if num % 2 == 1:
                if num > 3:
                    a_list.append(num)
                else:
                    a_list.append(-num)
a_list

# ### Functionally, with map/filter/sum

SMALL_NUM = 3
multiple_nums = filter(lambda nums: len(nums) > 1, num_lists)
flattened = sum(multiple_nums, [])
odds = filter(lambda num: num % 2 == 1, flattened)
small_becomes_negative = map(lambda num: -num if num < SMALL_NUM else num, odds)
a_list = list(small_becomes_negative)
a_list
