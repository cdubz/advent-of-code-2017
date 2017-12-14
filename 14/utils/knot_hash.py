from functools import reduce


def run_round(lengths, sparse_hash, pos=0, skip=0):
    max_len = len(sparse_hash)
    for length in lengths:
        pos %= max_len
        subset = list(
            reversed((sparse_hash + sparse_hash)[pos:(pos + length)]))
        for d in subset:
            pos %= max_len
            sparse_hash[pos] = d
            pos += 1
        pos += skip
        skip += 1
    return sparse_hash, pos % max_len, skip % max_len


def knot_hash(input):
    lengths = []
    if len(input) > 1:
        lengths += [ord(i) for i in input]
    lengths += [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    sparse_hash = list(range(0, 256))
    for i in range(0, 64):
        sparse_hash, pos, skip = run_round(
            lengths, sparse_hash, pos=pos, skip=skip)

    dense_hash = ''
    for i in range(0, int(len(sparse_hash) / 16)):
        chunk = sparse_hash[(i * 16):(i * 16 + 16)]
        dense_hash += '%0.2X'.lower() % reduce(lambda j, k: j ^ k, chunk)

    return dense_hash
