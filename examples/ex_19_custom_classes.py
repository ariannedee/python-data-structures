# # Creating custom classes
# Any custom class should:
# - Override the default `.__init__()`, `.__str__()` and `.__repr__()` methods
# - Use PascalCase for its name unless you have a good reason not to
# - Use the appropriate dunder methods, like `.__len__()`, instead of a custom `.get_length()` or `.length` attribute

class MyClass:
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        if hasattr(self.data, '__len__'):  # Does self.data.__len__() exist?
            return len(self.data)
        return 1
    
    def times_2(self):
        if hasattr(self.data, '__mul__'):
            return self.data * 2
        return self.data, self.data
    
    def __str__(self):
        return str(self.data)
        
    def __repr__(self):
        return f'MyClass({repr(self.data)})'


# +
data = [1, 2]       # Try different data 

mc = MyClass(data)  # Calls __init__
print(mc)           # Calls __str__
print([mc])         # Calls __repr__
print(len(mc))      # Calls __len__
print(mc.times_2())
# -

# ### Example: Custom Linked List

# +
class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            for i in iterable:
                self.append(i)

    def append(self, value):
        node = Node(value, self.head)
        self.head = node

    def pop(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            return node.value
        return None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def __repr__(self):
        aslist = [val for val in self]
        return f"LinkedList{repr(aslist)}"


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node
    
    def __repr__(self):
        return repr(self.value)
# -

ll = LinkedList('abc')
ll

ll.append('d')
ll

ll.pop()

ll

for val in ll:
    print(val)

# ## Inheriting from a class
# Say we want to be able to subtract one string for another. The `-` operator currently throws `TypeError`.

try:
    'abc' - 'b'
except Exception as e:
    print(repr(e))


# We can inherit from `str`, use `self` to access the string, and add/override any methods we want.

class mystr(str):
    def __sub__(self, other):
        result_list = [char for char in self if char not in other]
        return ''.join(result_list)


# To use it, wrap your string in the new class (create an instance of it).

test = mystr('abc')
test

test - 'b'

test.upper()

# ## Inheriting from a collection class
# The `collections` module has `UserDict`, `UserList` and `UserString` to inherit from.

# +
from collections import UserList

class MyList(UserList):
    def upper(self):
        new_data = []
        for val in self.data:
            if isinstance(val, str):
                new_data.append(val.upper())
            else:
                new_data.append(val)
        return MyList(new_data)
# -

l = MyList([1, 'a', 2, 'b'])
l

l.upper()

l[1]
