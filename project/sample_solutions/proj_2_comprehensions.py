# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'SQL', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift', 'Visual Basic',
             'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly', 'Kotlin', 'Dart', 'Scala',
             'Lua', 'Delphi', 'Haskell', 'Julia', 'Clojure', 'Elixir', 'Pascal']

# ## Load data

# +
import csv

with open('../data/Survey-2023:11:02.csv') as file:
    file.readline()
    reader = csv.DictReader(file, fieldnames=("timestamp", "languages", "years"))
    responses = [response['languages'].split(';') for response in reader]
    num_responses = len(responses)
    langs_known = [lang for langs in responses for lang in langs]

print(num_responses)
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**

langs_known_set = set(langs_known)
print(langs_known_set)

print(f"{len(langs_known_set)} / {len(all_langs)} languages known by this class ({round(len(langs_known_set) / len(all_langs) * 100)}%)")

# ## List languages not known by anyone in the class

not_known = set(all_langs) - langs_known_set
not_known_list = list(not_known)
not_known_list.sort()
print(not_known_list)

# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({percent_known}%)"`, in order from most to least known
#
# e.g. **1: Python (93%)**

langs_count = {lang: langs_known.count(lang) for lang in all_langs}
print(langs_count)

lang_count_list = list(langs_count.items())

lang_count_list.sort(key=lambda x: -x[1])

for pos, (lang, count) in enumerate(lang_count_list, start=1):
    percent_known = round(count / num_responses * 100)
    print(f"{pos}: {lang} ({percent_known}%)")


