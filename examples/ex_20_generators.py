# # Generator comprehensions
# If your main purpose is looping over a sequence and you don't need a list object, using a generator will save memory and can be a lot faster to run.

squares = (i ** 2 for i in range(10))
squares

for num in squares:
    print(num)

# Generators can only be looped over once

for num in squares:
    print(num)

# ## Comparing speed

from time import time

start = time()
big_gen = (i for i in range(10**10))
end = time()
f'Took {round(end - start, 4)}s'

start = time()
big_list = [i for i in range(10**7)]  # Initializing can take a long time and use a lot of memory
end = time()
f'Took {round(end - start, 4)}s'

# They can be used in certain functions without creating a list.
#
# `any()`, `all()`, `min()`, `max()` and `sum()` can all accept generators.

# +
from random import random

print(min((random() for i in range(10**4))))
print(max((random() for i in range(10**4))))
# -

# To create a tuple, cast a generator using the `tuple()`.

tuple((i for i in range(1, 30) if i % 3 == 0 or i % 5 == 0))
