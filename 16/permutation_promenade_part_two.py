"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be
dancing.

There are sixteen programs in total, named a through p. They start by standing
in a line: a stands in position 0, b stands in position 1, and so on until p,
which stands in position 15.

The programs' dance consists of a sequence of dance moves:

    Spin, written sX, makes X programs move from the end to the front, but
        maintain their order otherwise. (For example, s3 on abcde produces
        cdeab).
    Exchange, written xA/B, makes the programs at positions A and B swap
        places.
    Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do
the following dance:

    s1, a spin of size 1: eabcd.
    x3/4, swapping the last two programs: eabdc.
    pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle
input). In what order are the programs standing after their dance?
"""
from utils.move import move

pos = 1000000000
positions = list('abcdefghijklmnop')
movements = [v for v in open('input.txt').read().split(',')]

possibilities = [''.join(positions)]
for i in range(0, 100):
    positions = move(positions, movements)
    if ''.join(positions) in possibilities:
        break
    possibilities.append(''.join(positions))

answer_key = pos - int(pos/len(possibilities)) * len(possibilities)
print(answer_key)
print(''.join(possibilities[answer_key]))
