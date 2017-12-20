"""
--- Part Two ---

To simplify the problem further, the GPU would like to remove any particles that
collide. Particles collide if their positions ever exactly match. Because
particles are updated simultaneously, more than two particles can collide at the
same time and place. Once particles collide, they are removed and cannot collide
with anything else after that tick.

For example:

p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)
p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>

p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)
p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>

------destroyed by collision------
------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
------destroyed by collision------                      (3)
p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>

In this example, particles 0, 1, and 2 are simultaneously destroyed at the time
and place marked X. On the next tick, particle 3 passes through unharmed.

How many particles are left after all collisions are resolved?
"""
from utils.parse import parse

p = parse()
collided = []
tick = 0

while True:
    occupied = {}
    if tick > 1000:
        print(len(p) - len(collided))
        break
    for i in range(0, len(p)):
        if p[i]['x']:
            continue
        p[i]['v'][0] += p[i]['a'][0]
        p[i]['v'][1] += p[i]['a'][1]
        p[i]['v'][2] += p[i]['a'][2]
        p[i]['p'][0] += p[i]['v'][0]
        p[i]['p'][1] += p[i]['v'][1]
        p[i]['p'][2] += p[i]['v'][2]
        pos = ''.join([str(val) for val in p[i]['p']])
        if pos not in occupied.keys():
            occupied[pos] = []
        occupied[pos].append(p[i]['id'])

    for pos, ids in occupied.items():
        if len(ids) > 1:
            for i in ids:
                p[i]['x'] = True
                collided.append(id)

    tick += 1
