"""
--- Part Two ---

How many pixels stay on after 18 iterations?
"""
from utils.display import display
from utils.get_keys import get_keys
from utils.refactor import combine, divide

pattern = '.#./..#/###'
rules = {line.split(' => ')[0]: line.split(' => ')[1].strip() for line in
         open('input.txt').readlines()}

display(pattern)
for i in range(0, 18):
    print('---')
    parts = []
    for group in divide(pattern):
        for key in get_keys(group):
            if key in rules.keys():
                parts.append(rules[key])
                break
    pattern = combine(parts)
    display(pattern)
