def flip(pattern):
    if isinstance(pattern, str):
        pattern = str2list(pattern)
    flipped = []
    for line in pattern:
        flipped.append(reversed(line))
    return flipped


def list2str(l):
    s = ''
    for line in l:
        s += ''.join(line)
        s += '/'
    return s[:-1]


def rotate(l):
    return list(zip(*l[::-1]))


def str2list(s):
    l = []
    for line in s.split('/'):
        l.append(list(line))
    return l
