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
    reader = csv.DictReader(file, fieldnames=['timestamp', 'langs', 'years'])
    languages_known_by_person = [line['langs'].split(', ') for line in reader]

print(len(languages_known_by_person))
print(languages_known_by_person[0])
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**

# +
langs_known = {lang for langs in languages_known_by_person for lang in langs}
    
print(f"{len(langs_known)} / {len(all_langs)} languages known by this class (as {round(len(langs_known) / len(all_langs) * 100)}%)")
# -

# ## List languages not known by anyone in the class

set(all_langs) - langs_known

# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({percent_known}%)"`, in order from most to least known
#
# e.g. **1: Python (93%)**

# +
from collections import Counter
langs_count = Counter()

for langs in languages_known_by_person:
    langs_count.update(langs)
        
print(langs_count)
# -

num_people = len(languages_known_by_person)
for pos, (lang, count) in enumerate(langs_count.most_common(), start=1):
    print(f"{pos}: {lang} ({round(count / num_people * 100)}%)")
