def next_coords(spiral, x, y):
    n = x in spiral and (y + 1) in spiral[x]
    s = x in spiral and (y - 1) in spiral[x]
    e = (x + 1) in spiral and y in spiral[(x + 1)]
    w = (x - 1) in spiral and y in spiral[(x - 1)]

    if not any((n, s, e, w)):
        x += 1
    elif n and (not any((s, e, w)) or not e):
        x += 1
    elif s and (not any((n, e, w)) or e):
        x -= 1
    elif e and (not any((n, s, w)) or n):
        y -= 1
    elif w and (not any((n, s, e)) or not n):
        y += 1

    if x not in spiral:
        spiral[x] = {}

    return x, y
