def parse():
    particles = []
    i = 0
    with open('input.txt') as f:
        for line in f:
            data = line.rstrip().split('>, ')
            p = [int(v) for v in data[0][3:].split(',')]
            particles.append({
                'id': i,
                'p': p,
                'v': [int(v) for v in data[1][3:].split(',')],
                'a': [int(v) for v in data[2][3:len(data[2]) - 1].split(',')],
                'd': abs(p[0]) + abs(p[1]) + abs(p[2]),
                'x': False
            })
            i += 1
    return particles
