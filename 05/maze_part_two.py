"""
--- Part Two ---

Now, the jumps are even stranger: after each jump, if the offset was three or
more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the
offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""


def run():
    maze = {k: int(v) for k, v in enumerate(open('input.txt').read().split())}
    pos = 0
    steps = 0
    while True:
        try:
            move = maze[pos]
        except KeyError:
            print(steps)
            break
        last_pos = pos
        pos = last_pos + move
        if move >= 3:
            maze[last_pos] -= 1
        else:
            maze[last_pos] += 1
        steps += 1

if __name__ == '__main__':
    run()
