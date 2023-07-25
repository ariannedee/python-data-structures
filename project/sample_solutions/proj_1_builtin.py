# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

# +
all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'SQL', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift', 'Visual Basic',
             'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly', 'Kotlin', 'Dart', 'Scala',
             'Lua', 'Delphi', 'Haskell', 'Julia', 'Clojure', 'Elixir', 'Pascal']

print(len(all_langs))
# -

# ## Load data

# +
import csv

languages_known_by_person = []

with open('data/Programming language survey.csv') as file:
    file.readline()
    reader = csv.DictReader(file, fieldnames=['timestamp', 'langs', 'years'])
    for line in reader:
        languages_known_by_person.append(line['langs'].split(', '))

print(len(languages_known_by_person))
print(languages_known_by_person[0])
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**

# +
langs_known = set()
for langs in languages_known_by_person:
    langs_known.update(langs)

print(
    f"{len(langs_known)} / {len(all_langs)} languages known by this class (as {round(len(langs_known) / len(all_langs) * 100)}%)")
# -

# ## List languages not known by anyone in the class

set(all_langs) - langs_known

# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({percent_known}%)"`, in order from most to least known
#
# e.g. **1: Python (93%)**

# +
langs_count = {}
for langs in languages_known_by_person:
    for lang in langs:
        if lang not in langs_count:
            langs_count[lang] = 0

        langs_count[lang] += 1

print(langs_count)

# +
langs_count_by_frequency = list(langs_count.items())

langs_count_by_frequency.sort(key=lambda x: -x[1])
langs_count_by_frequency
# -

num_people = len(languages_known_by_person)
for pos, (lang, count) in enumerate(langs_count_by_frequency, start=1):
    print(f"{pos}: {lang} ({round(count / num_people * 100)}%)")


