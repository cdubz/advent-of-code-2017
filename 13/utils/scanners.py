def load_scanners():
    layers = {}
    layer = 0
    with open('input.txt') as f:
        for line in f:
            data = [int(i) for i in line.split(': ')]
            while layer != data[0]:
                layers[layer] = {'s': -1, 'd': -1, 'dir': None}
                layer += 1
            layers[data[0]] = {'s': 0, 'd': data[1], 'dir': 'down'}
            layer += 1
    return layers


def move_scanners(layers):
    for j in layers:
        if layers[j]['dir'] == 'down':
            if layers[j]['s'] < (layers[j]['d'] - 1):
                layers[j]['s'] += 1
            else:
                layers[j]['s'] -= 1
                layers[j]['dir'] = 'up'
        elif layers[j]['dir'] == 'up':
            if layers[j]['s'] > 0:
                layers[j]['s'] -= 1
            else:
                layers[j]['s'] += 1
                layers[j]['dir'] = 'down'
    return layers
