# # Survey analysis
# Analyse the results from the [languages survey](https://forms.gle/5b3mZRVcgAsoNG1FA)

all_langs = ['Python', 'Java', 'JavaScript', 'TypeScript', 'PHP', 'SQL', 'C', 'C++', 'C#',
             'Ruby', 'R', 'Matlab', 'Go', 'Rust', 'Objective-C', 'Swift', 'Visual Basic',
             'Perl', 'Cobol', 'Fortran', 'Lisp', 'Assembly', 'Kotlin', 'Dart', 'Scala',
             'Lua', 'Delphi', 'Haskell', 'Julia', 'Clojure', 'Elixir', 'Pascal']

# # Load data

# +
from pprint import pprint
import pandas as pd

filename = '../data/Programming language survey.csv'
df = pd.read_csv(filename, header=0, names=('timestamp', 'languages', 'other_langs', 'years'), usecols=('languages', 'other_langs', 'years'))
    
df.head()

# +
import re

for lang in all_langs:
    regex = rf'(^|;){re.escape(lang)}($|;)'
    df[lang] = df['languages'].str.contains(regex)
df
# -

# ## Find number of languages known
# Print `"{# known by class} / {# in list} languages known by this class (as %)"`.
#
# E.g. **12/21 languages known by this class (57%)**

known_langs = df.columns[df.eq(True).any()].tolist()
known_langs

percent = round(len(known_langs)/len(all_langs) * 100)
print(f"{len(known_langs)}/{len(all_langs)} languages known by this class ({percent}%)")

# ## List languages not known by anyone in the class

print('Not known:')
', '.join(df.columns[df.eq(False).all()].tolist())

# # Rank languages by most commonly known
# Print each language as `"{position}: {language} ({count})"`, in order from most to least known
#
# e.g. **1: Python (30)**

langs_count = df.iloc[:, 3:].sum()
langs_count

langs_count.sort_values(ascending=False, inplace=True)
langs_count

for i, (lang, count) in enumerate(langs_count.iteritems(), start=1):
    print(f'{i}: {lang} ({count})')

# ## Bonus: rank languages known by number of years programming

# +
year_ranges = ['< 1', '1 - 5', '5 - 10', '10 - 15', '15 - 20', '> 20', 'Unknown']

df2 = df
df2['years'] = pd.Categorical(df['years'], categories=year_ranges)
df2['years'].fillna("Unknown", inplace=True)
df2['total'] = 1
df2
# -

by_years = df2.groupby('years').sum()
by_years

for index in by_years.index:
    num_respondents = by_years.loc[index, 'total']
    print(f"For {index} ({num_respondents})")
    if num_respondents == 0:
        print('  No data')
    else:
        print(by_years.loc[index, by_years.loc[index] >= 1].sort_values(ascending=False).to_string())
    print()

# ## Bonus: other languages known

df3 = df.loc[:,['other_langs']]
df3

df3['other_langs'] = df3['other_langs'].str.split(',')
df3.dropna(axis=0, inplace=True)
other_langs = df3.explode('other_langs')
other_langs

other_langs.value_counts()


