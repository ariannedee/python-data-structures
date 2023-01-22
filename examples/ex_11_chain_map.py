# # collections.ChainMap
# Search through multiple dictionaries at once.

from collections import ChainMap

dict1 = {"one": 1, "two": 2, "three": 33}
dict2 = {"three": 3, "four": 4}

chain = ChainMap(dict1, dict2)
chain

# ## Key lookup
# Searches for keys in order.

chain["three"]

chain.get("four")

chain.get("five", "-")

# ## Updates
# Updating existing keys affects the first one found.

chain["three"] = -3
chain

del chain["three"]
chain

# Adding new items adds them to the first `dict`.

chain["six"] = 6
chain
