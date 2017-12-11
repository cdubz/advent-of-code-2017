def move(x, y, z, direction):
    if direction == 'n':
        x += 1
        z -= 1
    elif direction == 'ne':
        x += 1
        y -= 1
    elif direction == 'se':
        y -= 1
        z += 1
    elif direction == 's':
        x -= 1
        z += 1
    elif direction == 'sw':
        x -= 1
        y += 1
    elif direction == 'nw':
        y += 1
        z -= 1
    return x, y, z
