# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'SQL', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift', 'Visual Basic',
             'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly', 'Kotlin', 'Dart', 'Scala',
             'Lua', 'Delphi', 'Haskell', 'Julia', 'Clojure', 'Elixir', 'Pascal']

# ## Load data

# +
import csv

with open('../data/Programming language - responses.csv') as file:
    file.readline()
    reader = csv.DictReader(file, fieldnames=['timestamp', 'languages', 'years'])
    results = [lang for line in reader for lang in line['languages'].split(", ")]

print(len(results))
print(results)
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**

unique_langs = set(results)
num_known = len(unique_langs)
num_all = len(all_langs)
print(f"{num_known} / {num_all} languages known by this class ({round(num_known/num_all * 100)}%)")

# ## List languages not known by anyone in the class

not_known = set(all_langs) - unique_langs
print(not_known)

# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({percent_known}%)"`, in order from most to least known
#
# e.g. **1: Python (93%)**

# +
from collections import Counter

langs_by_count = Counter(results)
langs_by_count.update(not_known)
langs_by_count.subtract(not_known)
# -

for i, (lang, count) in enumerate(langs_by_count.most_common()):
    print(f"{i + 1}: {lang} ({count})")
