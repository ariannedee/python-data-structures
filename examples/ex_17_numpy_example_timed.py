# # Compare grades curving
# Compare NumPy ndarrays and Python lists/loops

import random
import time
import numpy as np

CURVE_CENTER = 80


# `timer()` is a decorator to log function execution times
#
# See Practical Decorators PyCon 2019 talk by Reuven M. Lerner to learn about decorators
# https://youtu.be/MjHpMCIvwsY?t=405

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        returned = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__.upper():<20} {end - start:f}s')
        return returned
    return inner


# ## Numpy functions
# Generate random grades

@timer
def np_grades(num):
    rg = np.random.default_rng(0)
    grades = rg.integers(20, 100, num)
    return grades


# Curve grades

@timer
def np_curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


# ## Looping functions
# Generate random grades

@timer
def loop_grades(num):
    grades = [random.randint(20, 100) for _ in range(num)]
    return grades


# Curve grades

@timer
def loop_curve(grades):
    average = sum(grades) / len(grades)
    change = CURVE_CENTER - average
    new_grades = [max(min(grade + change, 100), grade) for grade in grades]
    return new_grades


# ## Time comparison of numpy vs loops
# Time how long it takes to curve 10 up to 10,000,000 grades

for num_zeroes in range(2, 8):
    num_grades = 10 ** num_zeroes
    print(f'\n--- {num_grades:,} GRADES ---')
    
    np_curve(np_grades(num_grades)).tolist()  # Curve N grades with NumPy
    loop_curve(loop_grades(num_grades))       # Curve N grades with loops


