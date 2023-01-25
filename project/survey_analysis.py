# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift',
             'Visual Basic', 'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly']

# ## Load data

# +
import csv

with open('data/Programming language survey.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**



# ## List languages not known by anyone in the class



# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({count})"`, in order from most to least known
#
# e.g. **1: Python (30)**


