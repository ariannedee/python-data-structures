# # Deque
# A builtin linked list that can be used for stacks and queues.

from collections import deque

a = deque([1, 2, 3])
a

# ## Stack
# Last in, first out.
# ### Using the tail as the top of the stack
# Use `.append()` and `.pop()` to add/remove from the end of the `list`/`deque`.

last = a.pop()
last

a.append(4)
a

for _ in range(len(a)):
    print(a.pop())

try:
    a.pop()
except Exception as e:
    print(repr(e))

# ### Using the head as the top of the stack
# Use `.appendleft()` and `.popleft()` to add/remove from the front.

b = deque([1, 2, 3])
b

first = b.popleft()
first

b.appendleft(4)
b

for _ in range(len(b)):
    print(b.popleft())

try:
    a.popleft()
except Exception as e:
    print(repr(e))


# ## Create a custom stack or queue 
# They generally use **push** and **pop** as method names.
# ### Stack
# Last in, first out

class Stack(deque):
    def push(self, val):
        self.appendleft(val)
        
    def pop(self):
        return self.popleft()
    
    # If you want to remove methods, override it and use pass or raise an Exception


my_stack = Stack()
my_stack

for c in 'abcd':
    my_stack.push(c)
my_stack

my_stack.pop()

for _ in range(len(my_stack)):
    print(my_stack.pop())


# ### Custom queue
# First in, first out

class Queue(deque):
    def push(self, val):
        self.appendleft(val)
        
    # .pop() is already implemented
    
    # If you want to remove methods, override it and use pass or raise an Exception


my_q = Queue()
my_q

for c in 'abcd':
    my_q.push(c)
my_q

my_q.pop()

for _ in range(len(my_q)):
    print(my_q.pop())
