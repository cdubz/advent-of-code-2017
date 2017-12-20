"""
--- Part Two ---
The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

6 steps down (including the first line at the top of the diagram).
3 steps right.
4 steps up.
3 steps right.
4 steps down.
3 steps right.
2 steps up.
13 steps left (including the F it stops on).
This would result in a total of 38 steps.

How many steps does the packet need to go?
"""
tubes = {k: v.rstrip() for k, v in enumerate(open('input.txt').readlines())}
max_length = len(max([v for v in tubes.values()])) - 1
for k in tubes:
    tubes[k] = list(tubes[k])
    for i in range(len(tubes[k]) - 1, max_length):
        tubes[k].append(' ')

x, y = tubes[0].index('|'), 0
last = tubes[y][x]
x_dir, y_dir = 0, 1
letters = []
steps = 1

while True:
    x += x_dir
    y += y_dir
    steps += 1

    if tubes[y][x] == ' ':
        print(''.join(letters))
        print(steps - 1)
        break
    if tubes[y][x] not in ['|', '-', '+', ' ']:
        letters.append(tubes[y][x])
    elif tubes[y][x] == '+':
        if y_dir != 1 and y - 1 >= 0 and tubes[y - 1][x] != ' ':
            x_dir, y_dir = 0, -1
        elif x_dir != -1 and x + 1 < len(tubes[y]) and tubes[y][x + 1] != ' ':
            x_dir, y_dir = 1, 0
        elif y_dir != -1 and y + 1 < len(tubes) and tubes[y + 1][x] != ' ':
            x_dir, y_dir = 0, 1
        elif x_dir != 1 and x - 1 >= 0 and tubes[y][x - 1] != ' ':
            x_dir, y_dir = -1, 0
