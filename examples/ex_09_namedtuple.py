# # collections.namedtuple
#
# A lightweight class that acts like a tuple with a type name and attributes.

from collections import namedtuple

# Define a "class" with a name and attributes.

Coords = namedtuple("Location", "name lat lon")

# Create an "instance" of the class.

c = Coords('London', 42.99, -81.243)
c

# You can interact with the instance as if it were a tuple.

c[0]

# You can also access the named attributes.

c.name

c.lat

type(c)
