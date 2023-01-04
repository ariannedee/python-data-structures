"""
Curving grades example from https://realpython.com/numpy-tutorial/
"""
import numpy as np

CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])


def curve(grades):
    average = grades.mean()          # 60.75
    change = CURVE_CENTER - average  # 19.25
    new_grades = grades + change     # [91.25, 54.25, 83.25, 107.25, 70.25, 109.25, 93.25, 31.25]
    return np.clip(new_grades, grades, 100)  # [91.25, 54.25, 83.25, 100.0, 70.25, 100.0, 93.25, 31.25]


curve(grades)