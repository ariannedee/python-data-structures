all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift',
             'Visual Basic', 'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly']

# # Load data

# +
import csv
from pprint import pprint


langs_by_entry = []

with open('../data/Programming language survey.csv', 'r') as file:
    file.readline()
    reader = csv.DictReader(file, fieldnames=('timestamp', 'languages', 'other_langs', 'age'))
    for line in reader:
        langs_list = line['languages'].split(';')
        langs_by_entry.append(langs_list)

pprint(langs_by_entry)
# -

# ## Find number of languages known
# Print {# known by class} / {# in list} languages known by this class (as %).
# E.g. 12/21 languages known by this class (57%)

# +
known_langs = set()

for langs in langs_by_entry:
    known_langs.update(langs)

percent = round(len(known_langs)/len(all_langs) * 100)
print(f"{len(known_langs)}/{len(all_langs)} languages known by this class ({percent}%)")
# -

# ## List languages known and not known

print('Not known:')
print(set(all_langs) - known_langs)

# # Rank languages by most commonly known
# Print each language as `"{position}: {language} ({count})"`, in order from most to least known
#
# e.g. **1: Python (30)**

# +
rank_langs = {}
for langs in langs_by_entry:
    for lang in langs:
        rank_langs[lang] = rank_langs.get(lang, 0) + 1

rank_langs
# -

sorted_langs = sorted(list(rank_langs.items()), key=lambda tup: -tup[1])
sorted_langs

for i, (lang, count) in enumerate(sorted_langs, start=1):
    print(f"{i}: {lang} ({count})")


