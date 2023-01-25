# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift',
             'Visual Basic', 'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly']

# ## Load data

# +
import csv
from pprint import pprint

with open('../data/Programming language survey.csv') as file:
    file.readline()
    reader = csv.DictReader(file, fieldnames=('timestamp', 'languages', 'other_langs', 'age'))
    langs_by_entry = [line['languages'].split(';') for line in reader]

pprint(langs_by_entry)
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**

# +
langs_set = {lang for langs in langs_by_entry for lang in langs}

num_known = len(langs_set)
num_all = len(all_langs)
percent = round(num_known / num_all * 100)

print(f"{num_known} / {num_all} languages known by this class ({percent}%)")
# -

# ## List languages not known by anyone in the class

not_known = set(all_langs) - langs_set
print(not_known)

# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({count})"`, in order from most to least known
#
# e.g. **1: Python (30)**

from collections import Counter

langs_count = Counter([lang for langs in langs_by_entry for lang in langs])
langs_count

langs_count.most_common()

# +
num_people = len(langs_by_entry)

for i, (name, count) in enumerate(langs_count.most_common(), start=1):
    print(f"{i}: {name} ({round(count / num_people * 100)}%)")
