# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # List Comprehensions
#
# ## Basic comprehsions

# + jupyter={"outputs_hidden": false}
squares = [i ** 2 for i in range(10)]
squares
# -

# ### As for-loop

# + jupyter={"outputs_hidden": false}
squares = []
for i in range(10):
    squares.append(i ** 2)

squares
# -

# ## Using conditionals

# + jupyter={"outputs_hidden": false}
evens = [i for i in range(10) if i % 2 == 0]
evens
# -

# ### As for-loop

# + jupyter={"outputs_hidden": false}
evens = []

for i in range(10):
    if i % 2 == 0:
        evens.append(i)
evens
# -

# ## With ternary operator

# + jupyter={"outputs_hidden": false}
is_even = [True if i % 2 == 0 else False for i in range(10)]
is_even

# + jupyter={"outputs_hidden": false}
is_even = []
for i in range(10):
    if i % 2 == 1:
        is_even.append(True)
    else:
        is_even.append(False)
is_even
# -

# ## Nested comprehensions
#
# ### Nested lists

# + jupyter={"outputs_hidden": false}
coords = [
    [(x, y) for y in range(3)] for x in range(3)
]
coords
# -

# ### Looping over coords

# + jupyter={"outputs_hidden": false}
for row in coords:
    print(row)
# -

# ### As for-loop

# + jupyter={"outputs_hidden": false}
coords = []
for x in range(3):
    row = []
    for y in range(3):
        row.append((x, y))
    coords.append(row)
coords
# -

# ### Flattened list

# + jupyter={"outputs_hidden": false}
coords = [(x, y) for x in range(3) for y in range(3)]
coords
# -

# ### As for-loop

# + jupyter={"outputs_hidden": false}
coords = []
for x in range(3):
    for y in range(3):
        coords.append((x, y))
coords
# -

# ## Complex comprehension example

# + jupyter={"outputs_hidden": false}
num_lists = [[7, 2], [6], [1, 4, 5], [-2, 8, 0]]

# + jupyter={"outputs_hidden": false}
small_nums = [num
    for nums in num_lists
    for num in nums
    if num < 5]
small_nums
# -

# ### As for-loop

# + jupyter={"outputs_hidden": false}
small_nums = []
for nums in num_lists:
    for num in nums:
        if num < 5:
            small_nums.append(num)
small_nums
# -

# ## Very complex example

# + jupyter={"outputs_hidden": false}
num_lists = [[7, 2], [6], [1, 4, 5], [-2, 8, 0]]

# + jupyter={"outputs_hidden": false}
a_list = [num if num > 3 else -num
    for nums in num_lists
    if len(nums) > 1
    for num in nums
    if num % 2 == 1]
a_list
# -

# ### As for-loop

# + jupyter={"outputs_hidden": false}
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
# -

# ### Functionally, with map/filter/sum

# + jupyter={"outputs_hidden": false}
SMALL_NUM = 3
multiple_nums = filter(lambda nums: len(nums) > 1, num_lists)
flattened = sum(multiple_nums, [])
odds = filter(lambda num: num % 2 == 1, flattened)
small_becomes_negative = map(lambda num: -num if num < SMALL_NUM else num, odds)
a_list = list(small_becomes_negative)
a_list
