from .get_weight import get_weight


def debugger(program, responses, depth=0):
    weights = []
    for child in responses[program]['children']:
        if len(responses[child]['children']) > 0:
            debugger(child, responses, depth=(depth + 1))
            weights.append(get_weight(child, responses))
        else:
            weights.append(get_weight(child, responses))
    if len(set(weights)) > 1:
        dump_chain(program, responses, 0, weights)
        exit(1)


def dump_chain(program, responses, depth, highlight):
    weight = get_weight(program, responses)
    if weight in highlight:
        print(' ' * depth, '\033[91m' + str(weight) + '\033[00m', end='')
    else:
        print(' '*depth, weight, end='')
    print(' '*depth, '└', end='')
    print('┈'*depth, end='')
    print(program, end='')
    if weight != responses[program]['weight']:
        print(' ({})'.format(responses[program]['weight']), end='')
    print('\n', end='')
    for child in responses[program]['children']:
        dump_chain(child, responses, (depth+1), highlight)
