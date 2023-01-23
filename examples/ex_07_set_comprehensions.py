# # Set Comprehensions
# Just like `dict` comprehensions, but without a value expression (just key).
#
# Or just like `list` comprehensions, but using curly braces `{}`.
# ## Basic comprehensions

num_list = [1, 2, 3, 3, 8]
num_set = {num for num in num_list}
num_set

# This is equivalent to:

num_set = set(num_list)
num_set

# ## Nested comprehensions
# ### Nested set
# Sets can only contain hashable items.
#
# Since sets are mutable, if you want to nest sets, you must make any inner set an immutable `frozenset`.

words = ['mom', 'dad', 'add']
num_set = {
    frozenset({char for char in word})
    for word in words
}
num_set

# ### Flattened set

words = ['mom', 'dad', 'ham']
chars = {char for word in words for char in word}
chars

# ### As for-loop

chars = set()
for word in words:
    for char in word:
        chars.add(char)
chars

# ## Complex comprehension example

words = ['Mom', 'Dad', 'Ham']
consonants = {
    char
    for word in words
    for char in word.lower()
    if char not in 'aeiou'
}
consonants

# ### As for-loop

consonants = set()
for word in words:
    for char in word.lower():
        if char not in 'aeiou':
            consonants.add(char)
consonants
