from utils.transform import str2list


def display(pattern):
    if isinstance(pattern, str):
        pattern = str2list(pattern)
    s = []
    for line in pattern:
        s.append(''.join(line))
    print('\n'.join(s))
    print(''.join(s).count('#'))
