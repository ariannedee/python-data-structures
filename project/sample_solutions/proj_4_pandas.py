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
import pandas as pd


df = pd.read_csv("../data/Programming language survey.csv", header=0, names=("timestamp", "languages", "years"), usecols=("languages", "years"))
df.head()

# +
import re

# This regular expression checks if the string contains:
# - either the beginning of the string or a ", " delimeter
# - the name of the language (escaped because the + in C++ is a regex character)
# - either the end of the string or a ", " delimeter
# Note: the "?:" is to mark it as a 'match group' and is used to avoid warnings about captured groups
# See - https://stackoverflow.com/questions/39901550/python-userwarning-this-pattern-has-match-groups-to-actually-get-the-groups

for lang in all_langs:
    regex = rf'(?:^|, ){re.escape(lang)}(?:$|, )'
    df[lang] = df["languages"].str.contains(regex)
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

# ## Rank languages by most commonly known
# Print each language as `"{position}: {language} ({percent_known}%)"`, in order from most to least known
#
# e.g. **1: Python (93%)**

langs_count = df.iloc[:, 2:].sum()/len(df) * 100
langs_count

langs_count.sort_values(ascending=False, inplace=True)
langs_count

for i, (lang, count) in enumerate(langs_count.items(), start=1):
    print(f'{i}: {lang} ({round(count)}%)')

# ## Bonus: rank languages known by number of years programming
#

# +
year_ranges = ['< 1', '1 - 5', '5 - 10', '10 - 15', '15 - 20', '> 20', 'Unknown']

df2 = df
df2['years'] = pd.Categorical(df['years'], categories=year_ranges)
df2['years'].fillna("Unknown", inplace=True)
df2['total'] = 1
df2.head()
# -

by_years = df2.groupby('years', observed=False).sum(numeric_only=True)
by_years

for index in by_years.index:
    num_respondents = by_years.loc[index, 'total']
    print(f"For {index} ({num_respondents})")
    if num_respondents == 0:
        print('  No data')
    else:
        new_df = by_years.drop(columns=['total'])
        print(new_df.loc[index, new_df.loc[index] >= 1].sort_values(ascending=False).to_string())
    print()

# ## Bonus: show the breakdown of each language by number of years programming

for lang in all_langs:
    new_df = by_years.loc[:, [lang, 'total']]
    percent = new_df.loc[:, lang] / new_df.loc[:, 'total'] * 100
    new_df['percent'] = percent.astype(int)
    print(new_df.to_string())
    print()


