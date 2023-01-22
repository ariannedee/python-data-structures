# # collections.defaultdict
# A common pattern is to check if a key exists in a dictionary and initialize it if not.
# ## Without defaultdict

# +
countries = ["United States", "Mexico", "Iceland", "India", "Philippines", "Indonesia"]

letter_countries = {}
for country in countries:
    first_letter = country[0]
    if first_letter not in letter_countries:
        letter_countries[first_letter] = []
    letter_countries[first_letter].append(country)

letter_countries
# -

# ## With defaultdict

# +
from collections import defaultdict

letter_countries = defaultdict(list)
for country in countries:
    letter_countries[country[0]].append(country)

letter_countries
# -

# ## defaultdict
# Like regular dictionaries, but any missing keys have a default value if you try to access them.
#
# You can pass in any callable that doesn't have any required arguments.
#
# A callable can be:
# - a builtin function
# - a user-defined function
# - a lambda function
# - a class
# - a module function
# - an object's method

from collections import defaultdict

# ## Builtin functions
# The builtin types all have associated functions: `int`, `float`, `str`, `list`, `dict`, `tuple`, `set`.
#
# When you call them without arguments, they return an empty container or 0.

word_counts = defaultdict(int)
word_counts

word_counts['the']

word_counts

phrase = "the quick brown fox jumps over the lazy dog and the brown cat"
for word in phrase.split():
    word_counts[word] += 1
word_counts

# ## Custom functions
# You can define the function to call. It shouldn't take any arguments.

# +
count = 0

def get_count():
    global count
    count += 1
    return count

a = defaultdict(get_count)  # No brackets after function
for i in 'abcd':
    print(a[i])
    
a
# -

# ## Lambda functions
# For simple one-line functions that you won't need again, you can use lambda (anonymous) functions.

# +
b = defaultdict(lambda: [0, 0])

sprites = {'A': ['L', 'D', 'L', 'U'], 'B': ['R', 'U']}

for sprite, moves in sprites.items():
    for move in moves:
        if move == 'L':
            b[sprite][0] -= 1
        elif move == 'R':
            b[sprite][0] += 1
        elif move == 'D':
            b[sprite][1] -= 1
        elif move == 'U':
            b[sprite][1] += 1
        else:
            print(f"Invalid move {move}")
b


# -

# ## Class

# +
class Person:
    def __init__(self, name=''):
        self.name = name
        
    def __repr__(self):
        return f'Person("{self.name}")'

c = defaultdict(Person)

names = ["Aida", "Jia", "Lárus", "Idrissa"]
for i, name in enumerate(names):
    c[i].name = name

c
# -

# ## Module function

# +
from time import (
    time,   # Gets current time in secs since the Epoch (00:00 Jan 1, 1970 UTC)
    sleep,  # Wait n seconds
)

d = defaultdict(time)
for i in range(4):
    print(d[i])
    sleep(1)
d
# -


# ## Method
# I don't know a good reason to do this, but it can be done!

chars = "a b c".split()
e = defaultdict(chars.pop)
e[0]

chars.append('d')
chars

for i in range(3):
    print(e[i])
e

chars
