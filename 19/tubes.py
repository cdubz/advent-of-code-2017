"""
--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to follow a
routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -,
and +) show the path it needs to take, starting by going down onto the only line
connected to the top of the diagram. It needs to follow this path until it
reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue
going the same direction, and only turn left or right when there's no other
option. In addition, someone has left letters on the line; these also don't
change its direction, but it can use them to keep track of where it's been.
For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

Starting at the only line touching the top of the diagram, it must go down, pass
    through A, and continue onward to the first +.
Travel right, up, and right, passing through B in the process.
Continue down (collecting C), right, and up (collecting D).
Finally, go all the way left through E and stopping at F.
Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What
letters will it see (in the order it would see them) if it follows the path?
(The routing diagram is very wide; make sure you view it without line wrapping.)
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

while True:
    x += x_dir
    y += y_dir

    if tubes[y][x] == ' ':
        print(''.join(letters))
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
