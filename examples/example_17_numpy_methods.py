import numpy as np


# You can perform calculations on the whole array
a = np.array([
    (1, 2, 3),
    (4, 5, 6)
])
print(a.shape)  # (2, 3)

print("Whole array")
print(a.sum())
print(a.min())
print(a.max())

# If you pass an axis in, it calculates over that axis
print("Axis 0 (vertical)")
print(a.sum(0))
print(a.min(0))
print(a.max(0))

print("Axis 1 (horizontal)")
print(a.sum(1))
print(a.min(1))
print(a.max(1))

# Conversions
print(a.tolist())     # Return as Python (nested) lists
print(a.astype(str))  # Convert all items to a new type (e.g. strings)

# Changing shape
print(a.ravel())          # Flattened array
print(a.reshape((3, 2)))  # Modifies the shape
print(a.T)                # Returns the array transposed
