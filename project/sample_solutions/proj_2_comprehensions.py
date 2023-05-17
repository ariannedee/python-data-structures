# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'SQL', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift', 'Visual Basic',
             'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly', 'Kotlin', 'Dart', 'Scala',
             'Lua', 'Delphi', 'Haskell', 'Julia', 'Clojure', 'Elixir', 'Pascal']

# ## Load data

# +
import csv
from pprint import pprint

with open('../data/Programming language survey.csv') as file:
    file.readline()
    reader = csv.DictReader(file, fieldnames=('timestamp', 'languages', 'years'))
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
# Print each language as `"{position}: {language} ({percent_known}%)"`, in order from most to least known
#
# e.g. **1: Python (93%)**

# +
langs_list = [lang for langs in langs_by_entry for lang in langs]
langs_count = {lang: langs_list.count(lang) for lang in langs_set}

print(langs_count)


# +
def sort_func(x):
    return -x[1]


langs_count_list = list(langs_count.items())
langs_count_list.sort(key=sort_func)
langs_count_list

# +
num_people = len(langs_by_entry)

for i, (name, count) in enumerate(langs_count_list, start=1):
    print(f"{i}: {name} ({round(count / num_people * 100)}%)")
