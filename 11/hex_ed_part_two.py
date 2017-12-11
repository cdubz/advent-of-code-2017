"""
--- Part Two ---

How many steps away is the furthest he ever got from his starting position?
"""
from utils.move import move

path = open('input.txt').read().split(',')
furthest = 0
x, y, z = 0, 0, 0
for direction in path:
    x, y, z = move(x, y, z, direction)
    furthest = max(max(0 - x, 0 - y, 0 - z), furthest)
print(furthest)
